from airflow import DAG
from airflow.models.param import Param
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyTableOperator, BigQueryInsertJobOperator
from datetime import datetime

with DAG(
    dag_id="sensor_pipeline_with_create_table",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    params={"filename": Param("sensor-data.csv", type="string")},
    tags=["gcs", "bigquery", "create_table"]
) as dag:

    # 1️⃣ Create BigQuery Table (if not exists)
    create_table = BigQueryCreateEmptyTableOperator(
        task_id="create_sensor_data_table",
        project_id="zeta-flare-449207-r0",
        dataset_id="sensor_data",
        table_id="temperature_reading",
        schema_fields=[
            {"name": "temperature", "type": "FLOAT64"},
            {"name": "sensor1", "type": "FLOAT64"},
            {"name": "sensor2", "type": "FLOAT64"},
            {"name": "sensor3", "type": "FLOAT64"},
            {"name": "sensor4", "type": "FLOAT64"},
            {"name": "sensor5", "type": "FLOAT64"},
        ],
        exists_ok=True  # avoids failure if already created
    )

    # 2️⃣ Load data from GCS to BigQuery
    load_csv = GCSToBigQueryOperator(
        task_id="load_csv_to_bq",
        bucket="your-bucket-name",
        source_objects=["{{ params.filename }}"],
        destination_project_dataset_table="zeta-flare-449207-r0.sensor_data.temperature_reading",
        source_format="CSV",
        skip_leading_rows=1,
        write_disposition="WRITE_TRUNCATE",
        autodetect=False  # we defined schema above
    )

    # 3️⃣ Create aggregated table
    aggregate_data = BigQueryInsertJobOperator(
        task_id="aggregate_avg_reading",
        configuration={
            "query": {
                "query": """
                    CREATE OR REPLACE TABLE `zeta-flare-449207-r0.sensor_data.temperature_reading_avg` AS
                    SELECT
                      *,
                      ROUND((
                        sensor1 + sensor2 + sensor3 + sensor4 + sensor5
                      ) / 5, 2) AS avg_sensor_reading
                    FROM
                      `zeta-flare-449207-r0.sensor_data.temperature_reading`;
                """,
                "useLegacySql": False,
            }
        }
    )

    create_table >> load_csv >> aggregate_data
