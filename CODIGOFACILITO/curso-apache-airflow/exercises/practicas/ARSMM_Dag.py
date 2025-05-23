from airflow import DAG
from airflow.operators.dummmy_operator import DummyOperator
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
    'ARSMM_Dag',
    default_args = default_args,
    description = 'DAG Practica 2: Analisis de RRSS para marca de Moda',
    schedule_interval = None,
    start_date = datetime(2025,6,1),
    tag = ['Ingenieria']
) as dag:

    extrac_fb_api = DummyOperator(task_id = 'extrac_fb_api')
    extrac_tw_api = DummyOperator(task_id='extrac_tw_api')
    extrac_ig_api = DummyOperator(task_id='extrac_ig_api')

    trans_join_data = DummyOperator(task_id='trans_join_data')

    consumo_modelo_nlp = DummyOperator(task_id='consumo_modelo_nlp')

    ingest_db = DummyOperator(task_id='ingest_db')

    [extrac_fb_api, extrac_tw_api, extrac_ig_api] >> trans_join_data
    trans_join_data >> consumo_modelo_nlp
    consumo_modelo_nlp >> ingest_db
