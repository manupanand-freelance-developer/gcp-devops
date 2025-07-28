from airflow.models.param import Param

with DAG(
    dag_id="sensor_data_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    params={"filename": Param("sensor-data.csv", type="string")},
) as dag:

    load_csv = GCSToBigQueryOperator(
        task_id="load_csv_to_bigquery",
        bucket="your-bucket-name",
        source_objects=["{{ params.filename }}"],
        destination_project_dataset_table="zeta-flare-449207-r0.sensor_data.temperature_reading",
        source_format="CSV",
        skip_leading_rows=1,
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )
