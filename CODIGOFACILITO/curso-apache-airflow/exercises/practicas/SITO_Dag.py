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
    'SITO_Dag',
    default_args = default_args,
    description = 'DAG Practica 3: Sistema de Inventario para ina Tienda Online',
    schedule_interval = None,
    start_date = datetime(2025,6,1),
    tag = ['Ingenieria']
) as dag:

    extrac_inventario = DummyOperator(task_id = 'extrac_inventario')
    extrac_ventas = DummyOperator(task_id='extrac_ventas')
    extrac_compras = DummyOperator(task_id='extrac_compras')

    trans_join_data = DummyOperator(task_id='trans_join_data')

    consumo_modelo_ml = DummyOperator(task_id='consumo_modelo_ml')

    ingest_db = DummyOperator(task_id='ingest_db')
    email = DummyOperator(task_id='email')

    [extrac_inventario, extrac_ventas, extrac_compras] >> trans_join_data
    trans_join_data >> consumo_modelo_ml
    consumo_modelo_ml >> [ingest_db, email]
