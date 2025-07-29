resource "google_compute_network" "my_test_vpc" {
  name                    = "my-test-vpc"
  auto_create_subnetworks = false
}