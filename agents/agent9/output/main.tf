module "storage_account_1" {

  source = "../../../modules/storage_account"

  name                            = "exelixisstorageacct"
  location                        = "South India"
  resource_group_name             = "rg-demo"
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  account_kind                    = "StorageV2"
  allow_nested_items_to_be_public = false
  default_to_oauth_authentication = false
  tags = {
    Project = "dev"
  }

}

module "log_analytics_workspace_1" {

  source = "../../../modules/log_analytics_workspace"

  name                = "law-eva-fet"
  location            = "South India"
  resource_group_name = "rg-demo"
  tags = {
    Project = "Exelixis"
  }

}

module "application_insights_1" {

  source = "../../../modules/application_insights"

  name                = "appi-eva-dev"
  location            = "South India"
  resource_group_name = "rg-demo"
  application_type    = "web"
  sampling_percentage = 100
  tags = {
    Project = "Exelixis"
  }

}

module "service_plan_1" {

  source = "../../../modules/service_plan"

  name                = "asp-eva-dev"
  location            = "South India"
  resource_group_name = "rg-demo"
  os_type             = "Linux"
  sku_name            = "B1"
  tags = {
    Project = "Exelixis"
  }

}

module "linux_function_app_1" {

  source = "../../../modules/linux_function_app"

  name                                   = "func-linux-eva-dev"
  location                               = "South India"
  resource_group_name                    = "rg-demo"
  service_plan_id                        = module.service_plan_1.id
  storage_account_name                   = module.storage_account_1.name
  storage_account_access_key             = module.storage_account_1.primary_access_key
  application_insights_connection_string = module.application_insights_1.connection_string
  https_only                             = true
  builtin_logging_enabled                = true
  client_certificate_mode                = "Optional"
  ftps_state                             = "Disabled"
  python_version                         = "3.11"
  allowed_origins                        = ["*"]
  app_settings = {
    FUNCTIONS_WORKER_RUNTIME = "python"
    WEBSITE_RUN_FROM_PACKAGE = "1"
  }
  tags = {
    Project = "Exelixis"
  }

}

module "windows_function_app_1" {

  source = "../../../modules/windows_function_app"

  name                                   = "func-windows-eva-dev"
  location                               = "South India"
  resource_group_name                    = "rg-demo"
  service_plan_id                        = module.service_plan_1.id
  storage_account_name                   = module.storage_account_1.name
  storage_account_access_key             = module.storage_account_1.primary_access_key
  application_insights_connection_string = module.application_insights_1.connection_string
  https_only                             = true
  builtin_logging_enabled                = true
  client_certificate_mode                = "Optional"
  ftps_state                             = "Disabled"
  ip_restriction_default_action          = "Allow"
  allowed_origins                        = ["*"]
  app_settings = {
    FUNCTIONS_WORKER_RUNTIME = "dotnet"
    WEBSITE_RUN_FROM_PACKAGE = "1"
  }
  tags = {
    Project = "Exelixis"
  }

}