resource "google_artifact_registry_repository" "blp_test_repo" {
  location      = var.region
  repository_id = "blp-test-repo"
  description   = "docker repo to test cloud run"
  format        = "DOCKER"
}