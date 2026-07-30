module "application_insights_1" {

  source = "../../../modules/application_insights"

  name                = "appi-eva-dev"
  location            = "East US"
  resource_group_name = "rg-demo"
  application_type    = "web"
  sampling_percentage = 100
  tags = {
    Project = "Exelixis"
  }

}