from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from datetime import datetime
from airflow.operators.empty import EmptyOperator

# Configuration 
PROJECT_ID = "zeta-flare-449207-r0"
DATASET = "sensor_data"

# Default arguments
default_args = {
    "start_date": datetime(2024, 11, 18),
}

# DAG definition
with DAG(
    dag_id="create_bq_table",  # name of DAG
    default_args=default_args,
    schedule_interval=None,  # Trigger manually or as needed
    catchup=False,
    tags=["bigquery", "example"]
) as dag:

    start_task = EmptyOperator(task_id="start")
    end_task = EmptyOperator(task_id="end")

    # Create BigQuery table SQL
    create_bq_table = f"""
    CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET}.temperature_readings` (
        temperature STRING,
        sensor1 FLOAT64,
        sensor2 FLOAT64
    );
    """

    run_query_table = BigQueryExecuteQueryOperator(
        task_id="create_table",
        sql=create_bq_table,
        use_legacy_sql=False,
        location="asia-south1"  # optional: match your dataset location
    )

    start_task >> run_query_table >> end_task
