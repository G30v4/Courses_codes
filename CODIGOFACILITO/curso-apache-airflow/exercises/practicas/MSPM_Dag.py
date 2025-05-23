from airflow import DAG
from airflow.operators.dummmy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import task_group
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
    'MSPM_Dag',
    default_args = default_args,
    description = 'DAG Practica 4: Monitor de Sensores en una Planta de Manufactura',
    schedule_interval = '@hourly',
    start_date = datetime(2025,6,1),
    tag = ['Ingenieria']
) as dag:

    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')
    
    #def extract_sensor_data(sensor):
    #    print(f'Extrayendo datos del sensor {sensor}')
    
    @tastk_group(group_id='extract_sensor_data')
    def extract_sensor_data():
        #list_tasks_extract_sensor_data = []
        list_sensors = [f'sensor_{i}' for i in range(1,31)]
        for sensor in list_sensors:
            PythonOperator(
                task_id=f'extract_{sensor}',
                python_callable=lambda: print(f'Extrayendo datos del sensor {sensor}'),
                op_args=[sensor]
            )
            #list_tasks_extract_sensor_data.append(task)

    ingest_db = DummyOperator(task_id='ingest_db')

    trans_in_db_analisis = DummyOperator(task_id='trans_in_db_analisis')


    email_supervisores = DummyOperator(task_id='email_supervisores')
    email_mantenimiento = DummyOperator(task_id='email_mantenimiento')
    
    update_dash_mantenimiento = DummyOperator(task_id='update_dash_mantenimiento')
    update_dash_produccion = DummyOperator(task_id='update_dash_produccion')

    start >> extract_sensor_data() >> ingest_db >> trans_in_db_analisis
    trans_in_db_analisis >> [email_supervisores, 
                            email_mantenimiento, 
                            update_dash_mantenimiento, 
                            update_dash_produccion] >> end
