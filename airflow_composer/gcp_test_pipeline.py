# from airflow import DAG
# from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
# from datetime import datetime
# from airflow.operators.empty import EmptyOperator

# # Configuration 
# PROJECT_ID = "zeta-flare-449207-r0"
# DATASET = "sensor_data"

# # Default arguments
# default_args = {
#     "start_date": datetime(2024, 11, 18),
# }

# # DAG definition
# with DAG(
#     dag_id="create_bq_table",  # name of DAG
#     default_args=default_args,
#     schedule_interval=None,  # Trigger manually or as needed
#     catchup=False,
#     tags=["bigquery", "example"]
# ) as dag:

#     start_task = EmptyOperator(task_id="start")
#     end_task = EmptyOperator(task_id="end")

#     # Create BigQuery table SQL
#     create_bq_table = f"""
#     CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET}.temperature_readings` (
#         temperature STRING,
#         sensor1 FLOAT64,
#         sensor2 FLOAT64
#     );
#     """

#     run_query_table = BigQueryExecuteQueryOperator(
#         task_id="create_table",
#         sql=create_bq_table,
#         use_legacy_sql=False,
#         location="asia-south1"  # optional: match your dataset location
#     )

#     start_task >> run_query_table >> end_task

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

PROJECT_ID = "zeta-flare-449207-r0"
DATASET = "sensor_data"
TABLE = "temperature_readings"

default_args = {
    "start_date": datetime(2024, 11, 18),
}

with DAG(
    dag_id="create_bq_table_fallback",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=["bigquery"],
) as dag:

    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    create_bq_table = BigQueryInsertJobOperator(
        task_id="create_table",
        configuration={
            "query": {
                "query": f"""
                    CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET}.{TABLE}` (
                        temperature STRING,
                        sensor1 FLOAT64,
                        sensor2 FLOAT64
                    )
                """,
                "useLegacySql": False,
            }
        },
        location="asia-south1",  # Change this to your BQ dataset location if needed
    )

    start >> create_bq_table >> end
