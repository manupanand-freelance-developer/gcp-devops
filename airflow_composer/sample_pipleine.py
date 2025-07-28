from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

with DAG("gcs_to_bq_dag", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:

    load_to_bq = GCSToBigQueryOperator(
        task_id="load_csv_to_bq",
        bucket="your-bucket-name",
        source_objects=["path/to/data.csv"],
        destination_project_dataset_table="project.dataset.table",
        source_format="CSV",
        autodetect=True,
        write_disposition="WRITE_APPEND",
    )

    aggregate_job = BigQueryInsertJobOperator(
        task_id="aggregate_bq_data",
        configuration={
            "query": {
                "query": """
                    CREATE OR REPLACE TABLE dataset.aggregated AS
                    SELECT sensor_id, AVG(temperature) as avg_temp
                    FROM dataset.table
                    GROUP BY sensor_id
                """,
                "useLegacySql": False,
            }
        },
    )

    load_to_bq >> aggregate_job
