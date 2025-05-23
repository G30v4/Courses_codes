from airflow import DAG
from airflow.operators.dummmy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'G30v4',
    'depends_on_past': False,
    'email_on_failture': False,
    'email_on_retry': False,
    'retires': 1,
    'retry_delay': timedelta(seconds = 30)
}

with DAG(
    'SRP_DDag',
    default_args = default_args,
    description = 'DAG Practica 1: Recomendador de peliculas',
    schedule_interval = '@monthly',
    start_date = datetime(2025,6,1),
    tag = ['Ingenieria']
) as dag:

    extrac_db_inter = DummyOperator(task_id = 'extract_db_inter')
    extrac_api = DummyOperator(task_id='extract_api')

    trans_join_data = DummyOperator(task_id='trans_join_data')

    consumo_modelo_ml_api = DummyOperator(task_id='consumo_modelo_ml_api')

    send_email = DummyOperator(task_id='send_email')
    ingest_db = DummyOperator(task_id='ingest_db')

    [extrac_db_inter, extrac_api] >> trans_join_data
    trans_join_data >> consumo_modelo_ml_api
    consumo_modelo_ml_api >> [send_email, ingest_db]
