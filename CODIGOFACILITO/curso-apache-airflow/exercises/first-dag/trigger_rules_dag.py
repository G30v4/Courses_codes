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

def _extract1():
    print('Extract1')

def _extract2():
    print('Extract2')
    raise ValueError('Error in Extract2')

with DAG(
    'DAG_Triggers_rules',
    default_args = default_args,
    description = 'Ejemplo de Trigger Rules',
    schedule_interval = None,
    tag = ['Ingenieria', 'Triggers']
) as dag:

    start = DummyOperator(task_id = 'start' )

    extract1 = PythonOperator(
        task_id = 'extract1',
        python_callable = _extract1
    )

    extract2 = PythonOperator(
        task_id = 'extract1',
        python_callable = _extract2
    )

    # Trigger rule
    end = PythonOperator(
        task_id='end',
        python_callable = lambda: print('End'),
        trigger_rule = 'one_success'
    )

    start >> [extract1, extract2] >> end