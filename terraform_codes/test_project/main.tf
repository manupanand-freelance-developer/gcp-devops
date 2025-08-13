# module "artifacroty_registry" {
#   source = "./artifactory_registry"
#   af_region= var.af_region
# }
# module "vps" {
#   source = "./vpc"
# }
# 
module "bigquery" {
  source = "./bigquery"
  location = var.af_region
}