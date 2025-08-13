resource "google_bigquery_dataset" "sensor_data" {
  dataset_id                  = "sensor_data"
  description                 = "This is a test sensor data bigquery"
  location                    = var.location
  default_table_expiration_ms = 3600000

  labels = {
    env = "dev"
  }
}

resource "google_bigquery_table" "temperature_data" {
  dataset_id = google_bigquery_dataset.sensor_data.dataset_id
  table_id   = "temperature_data"

  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "dev"
  }

  schema = file("${path.module}schema.json")

}