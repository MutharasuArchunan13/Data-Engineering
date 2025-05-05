from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_hello():
    print("Hello from Airflow!")

def print_world():
    print("World from Airflow!")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='hello_airflow',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

    task2 = PythonOperator(
        task_id='print_world',
        python_callable=print_world
    )

    task1 >> task2  # Set task1 to run before task2
