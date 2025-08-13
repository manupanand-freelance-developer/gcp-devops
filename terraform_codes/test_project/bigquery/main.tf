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

  schema = <<EOF
[
  {
    "name": "temperature",
    "type": "FLOAT64",
    "mode": "NULLABLE",
    "description": "temperature in degree C"
  },
  {
    "name": "sensor1",
    "type": "FLOAT64",
    "mode": "NULLABLE",
    "description": "Sensor 1 data"
  },
  {
    "name": "sensor2",
    "type": "FLOAT64",
    "mode": "NULLABLE",
    "description": "Sensor 2 data"
  },
  {
    "name": "sensor3",
    "type": "FLOAT64",
    "mode": "NULLABLE",
    "description": "Sensor 3 data"
  },
  {
    "name": "sensor4",
    "type": "FLOAT64",
    "mode": "NULLABLE",
    "description": "Sensor 4 data"
  },
  {
    "name": "sensor5",
    "type": "FLOAT64",
    "mode": "NULLABLE",
    "description": "Sensor 5 data"
  }
  
  
]
EOF

}