from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'G30v4',
    'depends_on_past': False,
    'email_on_failture': False,
    'email_on_retry': False,
    'retires': 1
}

with DAG(
    'DAG_ETL_Dummy',
    default_args = default_args,
    description = 'Creacion de DAG para ETL',
    schedule_interval = None,
    tag = ['ETL', 'Ingenieria']
) as dag:

    get_api_bash = DummyOperator(task_id = 'get_api_bash')
    get_api_python = DummyOperator(task_id = 'get_api_python')

    join_trans = DummyOperator(task_id = 'join_trans')

    load_postgres = DummyOperator(task_id = 'load_postgres')

    [get_api_bash, get_api_python] >> join_trans >> load_postgres