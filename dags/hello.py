from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
                                                                  datetime.min.time())

default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2022,4,4),
        'email': ['jfibanezquiroz@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
  }

dag = DAG(dag_id='prueba_jose', default_args=default_args, schedule_interval='2 * * * *')
t1 = BashOperator(
    task_id='h1',
    bash_command='python /opt/airflow/codigo/Extract.py',
    dag=dag)

t1
