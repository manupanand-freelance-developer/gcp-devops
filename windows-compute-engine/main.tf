# Provider Configuration
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Variables - Hardcoded
variable "project_id" {
  description = "GCP Project ID"
  type        = string
  default     = "your-gcp-project-id"  # Replace with your actual project ID
}

variable "region" {
  description = "GCP Region"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "GCP Zone"
  type        = string
  default     = "us-central1-a"
}

# VPC Network
resource "google_compute_network" "vpc_network" {
  name                    = "custom-vpc-network"
  auto_create_subnetworks = false
  description             = "Custom VPC network for Windows Server"
}

# Subnet
resource "google_compute_subnetwork" "subnet" {
  name          = "custom-subnet"
  ip_cidr_range = "10.0.1.0/24"
  region        = var.region
  network       = google_compute_network.vpc_network.id
  description   = "Subnet for Windows Server instances"
}

# Firewall Rule - Allow RDP (Port 3389)
resource "google_compute_firewall" "allow_rdp" {
  name    = "allow-rdp"
  network = google_compute_network.vpc_network.name

  allow {
    protocol = "tcp"
    ports    = ["3389"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["windows-server"]
  description   = "Allow RDP access"
}

# Firewall Rule - Allow HTTP (Port 80)
resource "google_compute_firewall" "allow_http" {
  name    = "allow-http"
  network = google_compute_network.vpc_network.name

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["windows-server"]
  description   = "Allow HTTP access"
}

# Firewall Rule - Allow HTTPS (Port 443)
resource "google_compute_firewall" "allow_https" {
  name    = "allow-https"
  network = google_compute_network.vpc_network.name

  allow {
    protocol = "tcp"
    ports    = ["443"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["windows-server"]
  description   = "Allow HTTPS access"
}

# Firewall Rule - Allow SSH (Port 22)
resource "google_compute_firewall" "allow_ssh" {
  name    = "allow-ssh"
  network = google_compute_network.vpc_network.name

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["windows-server"]
  description   = "Allow SSH access"
}

# Firewall Rule - Allow MongoDB (Port 27017)
resource "google_compute_firewall" "allow_mongodb" {
  name    = "allow-mongodb"
  network = google_compute_network.vpc_network.name

  allow {
    protocol = "tcp"
    ports    = ["27017"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["windows-server"]
  description   = "Allow MongoDB access"
}

# Firewall Rule - Allow ICMP (Ping)
resource "google_compute_firewall" "allow_icmp" {
  name    = "allow-icmp"
  network = google_compute_network.vpc_network.name

  allow {
    protocol = "icmp"
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["windows-server"]
  description   = "Allow ICMP from anywhere"
}

# Windows Server 2022 Instance
resource "google_compute_instance" "windows_server" {
  name         = "windows-server-2022"
  machine_type = "e2-medium"
  zone         = var.zone

  tags = ["windows-server"]

  boot_disk {
    initialize_params {
      image = "windows-server-2022-dc-v20241009"
      size  = 50
      type  = "pd-standard"
    }
  }

  network_interface {
    network    = google_compute_network.vpc_network.name
    subnetwork = google_compute_subnetwork.subnet.name

    access_config {
      # Ephemeral external IP
    }
  }

  # Allow Windows to configure on first boot
  metadata = {
    windows-startup-script-ps1 = <<-EOT
      # Enable RDP
      Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -Value 0
      Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
      EOT
  }

  # Service account with default scopes
  service_account {
    scopes = ["cloud-platform"]
  }
}

# Outputs
output "instance_name" {
  value       = google_compute_instance.windows_server.name
  description = "Name of the Windows Server instance"
}

output "instance_external_ip" {
  value       = google_compute_instance.windows_server.network_interface[0].access_config[0].nat_ip
  description = "External IP address of the Windows Server"
}

output "instance_internal_ip" {
  value       = google_compute_instance.windows_server.network_interface[0].network_ip
  description = "Internal IP address of the Windows Server"
}

output "vpc_network_name" {
  value       = google_compute_network.vpc_network.name
  description = "Name of the VPC network"
}

output "subnet_name" {
  value       = google_compute_subnetwork.subnet.name
  description = "Name of the subnet"
}

output "rdp_command" {
  value       = "Use RDP client to connect to: ${google_compute_instance.windows_server.network_interface[0].access_config[0].nat_ip}:3389"
  description = "RDP connection command"
}