resource "google_compute_instance" "test_instance" {
  name           = "my-test-instance"
  machine_type   =  "n1-standard-1"
  zone           = "asia-south1-a"
  
  tags= ["dev"]
  boot_disk{
    initialize_params {
      image = data.google_compute_image.ubuntu_image.
      size  = 30 # size in GB 
    }
  }
  network_interface {
     network = "default"  # or your custom network
     access_config {}     # enables external IP
   }
 
   metadata_startup_script = <<-EOT
     #!/bin/bash
     apt-get update && apt-get install -y nginx
   EOT
}