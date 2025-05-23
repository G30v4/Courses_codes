from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummmy_operator import DummyOperator

## GPC Providers
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecutorQueryOperator


from datetime import datetime, timedelta

# Functions
def _extract_data(platform, ti, **kwargs):
    import requests
    # API Params: Date:: M/D/Y
    # Airflow format:: Y/M/D
    start_date = kwargs['data_interval_start'].strftime('%-m/%-d/%Y')
    end_date = kwargs['data_interval_end'].strftime('%-m/%-d/%Y')
    url = f'api_url_campaing?start_date={start_date}&end_date={end_date}'
    headers = {'X-API-Key': 'api_key'}
    response = requests.get(url, headers=headers)
    tmp_file = f'marketing_stats_{platform}_{kwargs["ds_nodash"]}_{kwargs["next_ds_nodash"]}.csv'
    tmp_path = f'/tmp/{tmp_file}'
    with open(tmp_path, 'wb') as file:
        file.write(response.content)
        file.close()
    ti.xcom_push(key=f'tmp_file_{platform}', value=tmp_file)
    ti.xcom_push(key=f'tmp_path_{platform}', value=tmp_path)


default_args = {
    'owner': 'G30v4',
    'depends_on_past': False,
    'email_on_failture': False,
    'email_on_retry': False,
    'retires': 1,
    'retry_delay': timedelta(seconds = 30)
}

with DAG(
    'Marketing_ETL_Dag_v2',
    default_args = default_args,
    description = 'DAG Providers ej1: Marketing ETL',
    schedule_interval = '@monthly',
    start_date = datetime(2025,5,22),
    tag = ['Ingenieria']
) as dag:

    start = DummyOperator(task_id = 'start')
    end = DummyOperator(task_id = 'end')

    # Platforms: google ads, facebook ads
    gads_extract = PythonOperator(
        task_id = 'gads_extract',
        python_callable = _extract_data,
        op_kwargs = {'platform': 'gads'}
    )

    fads_extract = PythonOperator(
        task_id = 'fads_extract',
        python_callable = _extract_data,
        op_kwargs = {'platform': 'fads'}
    )

    yads_extract = PythonOperator(
        task_id = 'yads_extract',
        python_callable = _extract_data,
        op_kwargs = {'platform': 'yads'}
    )

    transf_gads = LocalFilesystemToGCSOperator(
        task_id = 'transf_gads',
        src = '{{ti.xcom_pull(key="tmp_path_gads")}}',
        dst = f'marketing_data/'+'{{ti.xcom_pull(key="tmp_file_gads")}}',
        bucket = 'my-gpc-bucket-etl'
        gcp_conn_id = 'my_gcp_conn'
    )

    transf_fads = LocalFilesystemToGCSOperator(
        task_id = 'transf_fads',
        src = '{{ti.xcom_pull(key="tmp_path_fads")}}',
        dst = f'marketing_data/'+'{{ti.xcom_pull(key="tmp_file_fads")}}',
        bucket = 'my-gpc-bucket-etl'
        gcp_conn_id = 'my_gcp_conn'
    )

    transf_yads = LocalFilesystemToGCSOperator(
        task_id = 'transf_yads',
        src = '{{ti.xcom_pull(key="tmp_path_yads")}}',
        dst = f'marketing_data/'+'{{ti.xcom_pull(key="tmp_file_yads")}}',
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
        source_objects = [f'marketing_data/'+'{{ti.xcom_pull(key="tmp_file_gads")}}'],
        destination_project_dataset_table = 'marketing.gads',
        schema_fields = schema_fields,
        write_disposition = 'WRITE_TRUNCATE',
        skip_leading_rows = 1,
        gcp_conn_id = 'my_gcp_conn'
    )

    fads_bigquery = GCSToBigQueryOperator(
        task_id = 'fads_bigquery',
        bucket = 'my-gpc-bucket-etl',
        source_objects = [f'marketing_data/'+'{{ti.xcom_pull(key="tmp_file_fads")}}'],
        destination_project_dataset_table = 'marketing.fads',
        schema_fields = schema_fields,
        write_disposition = 'WRITE_TRUNCATE',
        skip_leading_rows = 1,
        gcp_conn_id = 'my_gcp_conn'
    )

    yads_bigquery = GCSToBigQueryOperator(
        task_id = 'yads_bigquery',
        bucket = 'my-gpc-bucket-etl',
        source_objects = [f'marketing_data/'+'{{ti.xcom_pull(key="tmp_file_yads")}}'],
        destination_project_dataset_table = 'marketing.yads',
        schema_fields = schema_fields,
        write_disposition = 'WRITE_APPEND',
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
