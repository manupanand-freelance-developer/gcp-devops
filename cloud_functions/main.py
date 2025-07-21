from google.cloud import bigquery
import os

def load_csv_to_bq(event, context):
    # Get the file info
    bucket = event['bucket']
    file = event['name']
    uri = f"gs://{bucket}/{file}"

    # Define BQ target
    dataset_id = os.environ["DATASET_ID"]
    table_id = os.environ["TABLE_ID"]

    # Load config
    client = bigquery.Client()
    table_ref = f"{client.project}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        autodetect=True,
        skip_leading_rows=1,
    )

    load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
    load_job.result()

    print(f"Loaded {uri} into {table_ref}")


def main():
    # Example event dict for local testing
    event = {
        "bucket": "your-gcs-bucket-name",
        "name": "path/to/your.csv"
    }
    context = None  # or a mock object if needed
    load_csv_to_bq(event, context)


if __name__ == "__main__":
    main()
