from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'G30v4',
    'depends_on_past': False,
    'email_on_failture': False,
    'email_on_retry': False,
    'retires': 1,
    'retry_delay': timedelta(minutes = 2)
}

# Functions

def _get_api():
    import request
    url = 'api_url'
    headers = {'X-API-Key': 'api_key'}
    response = requests.get(url, headers=headers)
    with open('/tmp/sales_db_py.csv', 'wb') as file:
        file.write(response.content)
        file.close()

def _join_trans():
    import pandas as pd
    df_py = pd.read_csv('/tmp/sales_db_py.csv')
    df_bash = pd.read_csv('/tmp/sales_db_bash.csv')
    df = pd.concat([df_py, df_bash], ignore_index=True)
    df = df.groupby(['date', 'store'])['sales'].sum().reset_index()
    df = df.rename(columns={'date': 'ddate'})
    df.to_csv('/tmp/sales_db.csv', sep='\t', index=False, header=False)
    print(df.head())

def _load_data():
    from airflow.providers.postgres.hooks.postgres import PostgresHook
    pg_hook = PostgresHook(postgres_conn_id = 'mydb_conn')
    pg_hook.bulk_load(table= 'sales_db', tmp_file='/tmp/sales_db.csv')

with DAG(
    'DAG_ETL_PostgreSQL',
    default_args = default_args,
    description = 'Creacion de DAG para ETL de PostgreSQL',
    schedule_interval = None,
    tag = ['ETL', 'Ingenieria', 'PostgreSQL']
) as dag:

    get_api_python = PythonOperator(
        task_id = 'get_api_python',
        python_callable = _get_api
    )

    get_api_bash = BashOperator(
        task_id = 'get_api_bash',
        python_callable = 'curl -H "X-API-Key: api-key" url' > /tmp/sales_db_bash.csv
    )

    join_trans = PythonOperator(
        task_id = 'join_trans',
        python_callable = _join_trans
    )

    check_table = PostgresOperator(
        task_id = 'check_table',
        postgres_conn_id = 'mydb_conn'
        sql = "sql/create_table.sql"
    )

    load_data = PythonOperator(
        task_id = 'load_data',
        python_callable = _load_data
    )

    [get_api_bash, get_api_python] >> join_trans >> check_table >> load_data
