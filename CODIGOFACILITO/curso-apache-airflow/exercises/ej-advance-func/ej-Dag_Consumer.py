from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummmy_operator import DummyOperator
from airflow.sensors.external_task import ExternalTaskSensor

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
    'DAG_Analitica_MKT',
    default_args = default_args,
    description = 'DAG Sensors ej1: Analitica y sensors',
    schedule_interval = '@daily',
    start_date = datetime(2025,5,22),
    tag = ['Ingenieria']
) as dag:

    start = DummyOperator(task_id = 'start')

    sensor_DB_Ventas_Raw = ExternalTaskSensor(
        task_id = 'sensor_DB_Ventas_Raw',
        external_dag_id = 'DAG_Ventas',
        external_task_id = 'transfer2',
        allowed_states = ['success']
    )

    mkt_data = DummyOperator(task_id = 'mkt_data')

    join_transform = DummyOperator(task_id = 'join_transform')

    ingest = DummyOperator(task_id = 'ingest')

    end = DummyOperator(task_id = 'end')

    start >> [sensor_DB_Ventas_Raw, mkt_data] >> join_transform >> ingest >> end
