from airflow import DAG
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
    'DAG_Template_Info',
    default_args = default_args,
    description = 'DAG Advance Funct ej1: Seguimiento del Context',
    schedule_interval = None,
    tag = ['Ingenieria']
) as dag:

    def print_context(**kwargs):
        for key, value in kwargs.items():
            print(f"Key: {key} - value: {value} - Type: {type(value)}")

    task_print_context = PythonOperator(
        task_id = 'task_print_context',
        python_callable = print_context
    )

    task_print_context
