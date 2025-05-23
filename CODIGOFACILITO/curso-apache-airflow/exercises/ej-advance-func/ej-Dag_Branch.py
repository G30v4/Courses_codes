from airflow import DAG

from airflow.operators.dummmy_operator import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator

import random
from datetime import datetime, timedelta

default_args = {
    'owner': 'G30v4',
    'depends_on_past': False,
    'email_on_failture': False,
    'email_on_retry': False,
    'retires': 1,
    'retry_delay': timedelta(seconds = 30)
}

# Functions
def _extract():
    print('Extracting data')
    print('Counting data')
    return random.randint(1,10)

def _branch(**kwargs):
    ti = kwargs['ti']
    row = ti.xcom_pull(task_id = 'extract')
    if row > 5:
        return 'transform1'
    return 'predict_lost_data'

with DAG(
    'DAG_Branch,
    default_args = default_args,
    description = 'DAG Branch ej1: Analitica y sensors',
    schedule_interval = '@daily',
    start_date = datetime(2025,5,22),
    tag = ['Ingenieria']
) as dag:

    start = DummyOperator(task_id = "start")

    extract = PythonOperator(
        task_id = 'extract',
        python_callable = _extract
    )

    branch_task = BranchPythonOperator(
        task_id = 'branch_task',
        python_callable = _branch
    )

    transform1 = DummyOperator(task_id = 'transform1')

    predict_lost_data = DummyOperator(task_id = 'predict_lost_data')

    transform2 = DummyOperator(task_id = 'transform2')

    ingest = DummyOperator(
        task_id = 'ingest',
        trigger_rule = 'one_success'
    )

    end = DummyOperator(task_id = "end")

    start >> extract >> branch_task
    branch_task >> transform1
    branch_task >> predict_lost_data >> transform2
    [transform1, transform2] >> ingest >> end