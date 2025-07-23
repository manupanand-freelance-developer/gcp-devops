import csv 
import os 
from  google.cloud import storage,bigquery 

def gcs_to_bigquery(event,context):
    bucket_name = event['bucket']
    file_name = event['name']
    
    storage_client = storage.Client()
    bq_client = bigquery.Client()
    
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    contents = blob.download_as_text().splitlines()
    reader = csv.DictReader(contents)
    
    dataset_id= os.environ["BQ_DATASET"]
    table_id=os.environ["BQ_TABLE"]
    table_ref=f"{bq_client.project}.{dataset_id}.{table_id}"
    
    row_to_insert = [ row for row in reader ]
    errors = bq_client.insert_rows_json(table_ref,row_to_insert)
    if errors:
            print("❗ Errors while inserting: ", errors)
    else:
            print("Inserted ")

    