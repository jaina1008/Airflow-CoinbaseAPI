from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import dats_ago
from datetime import datetime
from coinbase import coinbase_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['myemail@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


dag = DAG(
    'coinbase_dag',
    default_args=default_args,
    description='ETL from Coinbase'
)

run_etl = PythonOperator(
    task_id='task_coinbase_etl',
    python_callable=coinbase_etl,
    dag=dag
)

run_etl
