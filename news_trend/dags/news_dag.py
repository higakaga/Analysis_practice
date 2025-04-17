from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from utils import path_setup

from fetch_news import get_news
from run_news_pipeline import run_keyword_extraction

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='news_pipeline_daily',
    default_args=default_args,
    schedule_interval='0 9 * * *',  # 매일 오전 9시
    catchup=False
) as dag:

    task_fetch_news = PythonOperator(
        task_id='fetch_naver_news',
        python_callable=get_news,
        op_args=['대선']
    )

    task_run_pipeline = PythonOperator(
        task_id='extract_keywords',
        python_callable=run_keyword_extraction
    )

    task_fetch_news >> task_run_pipeline
