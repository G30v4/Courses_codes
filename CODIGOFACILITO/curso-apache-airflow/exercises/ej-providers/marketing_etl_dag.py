from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummmy_operator import DummyOperator

## GPC Providers
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecutorQueryOperator


from datetime import datetime, timedelta

# Functions
def _extract_data(platform):
    import requests
    url = 'api_url_campaing'
    headers = {'X-API-Key': 'api_key'}
    response = requests.get(url, headers=headers)
    with open('/tmp/marketing_stats_{platform}.csv', 'wb') as file:
        file.write(response.content)
        file.close()


default_args = {
    'owner': 'G30v4',
    'depends_on_past': False,
    'email_on_failture': False,
    'email_on_retry': False,
    'retires': 1,
    'retry_delay': timedelta(seconds = 30)
}

with DAG(
    'Marketing_ETL_Dag',
    default_args = default_args,
    description = 'DAG Providers ej1: Marketing ETL',
    schedule_interval = None,
    start_date = datetime(2025,6,1),
    tag = ['Ingenieria']
) as dag:

    start = DummyOperator(task_id = 'start')
    end = DummyOperator(task_id = 'end')

    # Platforms: google ads, facebook ads
    gads_extract = PythonOperator(
        task_id = 'gads_extract',
        python_callable = _extract_data,
        default_args = ['gads']
    )

    fads_extract = PythonOperator(
        task_id = 'fads_extract',
        python_callable = _extract_data,
        default_args = ['fads']
    )

    yads_extract = PythonOperator(
        task_id = 'yads_extract',
        python_callable = _extract_data,
        default_args = ['yads']
    )

    transf_gads = LocalFilesystemToGCSOperator(
        task_id = 'transf_gads',
        src = '/tmp/marketing_stats_gads.csv',
        dst = 'marketing_data/marketing_stats_gads.csv',
        bucket = 'my-gpc-bucket-etl'
        gcp_conn_id = 'my_gcp_conn'
    )

    transf_fads = LocalFilesystemToGCSOperator(
        task_id = 'transf_fads',
        src = '/tmp/marketing_stats_fads.csv',
        dst = 'marketing_data/marketing_stats_fads.csv',
        bucket = 'my-gpc-bucket-etl'
        gcp_conn_id = 'my_gcp_conn'
    )

    transf_yads = LocalFilesystemToGCSOperator(
        task_id = 'transf_yads',
        src = '/tmp/marketing_stats_yads.csv',
        dst = 'marketing_data/marketing_stats_yads.csv',
        bucket = 'my-gpc-bucket-etl'
        gcp_conn_id = 'my_gcp_conn'
    )

    # To BigQuery
    schema_fields = [
        {'name': 'date', 'type': 'DATE'},
        {'name': 'country', 'type': 'STRING'},
        {'name': 'city', 'type': 'STRING'},
        {'name': 'gender', 'type': 'STRING'},
        {'name': 'campaign', 'type': 'STRING'},
        {'name': 'clicks', 'type': 'INTEGER'},
        {'name': 'views', 'type': 'INTEGER'},
        {'name': 'sales', 'type': 'FLOAT'},
        {'name': 'cost', 'type': 'FLOAT'}
    ]

    gads_bigquery = GCSToBigQueryOperator(
        task_id = 'gads_bigquery',
        bucket = 'my-gpc-bucket-etl',
        source_objects = ['marketing_data/marketing_stats_gads.csv'],
        destination_project_dataset_table = 'marketing.gads',
        schema_fields = schema_fields,
        write_disposition = 'WRITE_TRUNCATE',
        skip_leading_rows = 1,
        gcp_conn_id = 'my_gcp_conn'
    )

    fads_bigquery = GCSToBigQueryOperator(
        task_id = 'fads_bigquery',
        bucket = 'my-gpc-bucket-etl',
        source_objects = ['marketing_data/marketing_stats_fads.csv'],
        destination_project_dataset_table = 'marketing.fads',
        schema_fields = schema_fields,
        write_disposition = 'WRITE_TRUNCATE',
        skip_leading_rows = 1,
        gcp_conn_id = 'my_gcp_conn'
    )

    yads_bigquery = GCSToBigQueryOperator(
        task_id = 'yads_bigquery',
        bucket = 'my-gpc-bucket-etl',
        source_objects = ['marketing_data/marketing_stats_yads.csv'],
        destination_project_dataset_table = 'marketing.yads',
        schema_fields = schema_fields,
        write_disposition = 'WRITE_TRUNCATE',
        skip_leading_rows = 1,
        gcp_conn_id = 'my_gcp_conn'
    )

    ## Group Data

    group_query = """
        CREATE OR REPLACE TABLE 'my-big-query-123.marketing.insights' AS
        SELECT date, campaign, 'gads' as platform,
        sum(clicks) as clicks, sum(views) as views, sum(sales) as sales, sum(cost) as cost
        FROM 'my-big-query-123.marketing.gads'
        group by 1,2
        union all
        SELECT date, campaign, 'fads' as platform,
        sum(clicks) as clicks, sum(views) as views, sum(sales) as sales, sum(cost) as cost
        FROM 'my-big-query-123.marketing.fads'
        group by 1,2
        union all
        SELECT date, campaign, 'yads' as platform,
        sum(clicks) as clicks, sum(views) as views, sum(sales) as sales, sum(cost) as cost
        FROM 'my-big-query-123.marketing.yads'
        group by 1,2
    """

    create_view = BigQueryExecutorQueryOperator(
        task_id = 'create_view',
        sql = group_query,
        use_legacy_sql = False,
        gcp_conn_id = 'my_gcp_conn'
    )




    start >> [gads_extract, fads_extract, yads_extract]
    transf_gads >> gads_bigquery
    gads_extract >> transf_gads >> gads_bigquery
    fads_extract >> transf_fads >> fads_bigquery
    yads_extract >> transf_yads >> yads_bigquery
    [gads_bigquery, fads_bigquery, yads_bigquery] >> create_view >> end
