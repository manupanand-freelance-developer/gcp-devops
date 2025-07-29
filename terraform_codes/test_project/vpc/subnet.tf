resource "google_compute_subnetwork" "my_subnet_asia" {
  name              = "asia-subnet-mumbai"
  ip_cidr_range     = "192.168.0.0/16"
  region            = "asia-south1"
  network           = google_compute_network.my_test_vpc.id
}