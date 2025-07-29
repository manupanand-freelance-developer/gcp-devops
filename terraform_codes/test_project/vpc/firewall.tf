resource "google_compute_firewall" "allow_ssh" {
  name            ="allow-ssh"
  network         =google_compute_network.my_test_vpc.id
  allow {
    protocol      = "tcp"
    ports         = ["22"]
  }
  priority        =  1000
  source_ranges   = ["0.0.0.0/0 "]
}