from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
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
    'DAG_Ventas',
    default_args = default_args,
    description = 'DAG Sensors ej1: Ventas',
    schedule_interval = '@daily',
    start_date = datetime(2025,5,22),
    tag = ['Ingenieria']
) as dag:

    start = DummyOperator(task_id = 'start')

    extract = DummyOperator(task_id = 'extract')

    transform1 = DummyOperator(task_id = 'transform1')

    transform2 = BashOperator(
        task_id = 'transform2',
        bash_command = 'sleep 5'
    )

    ingest1 = DummyOperator(task_id = 'ingest1')
    ingest2 = DummyOperator(task_id = 'ingest2')

    end = DummyOperator(task_id = 'end')

    start >> extract >> [transform1, transform2]
    transform1 >> ingest1
    transform2 >> ingest2
    [ingest1, ingest2] >> end