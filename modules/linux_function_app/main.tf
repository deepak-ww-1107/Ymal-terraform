resource "azurerm_linux_function_app" "this" {
  name                = var.name
  location            = var.location
  resource_group_name = var.resource_group_name

  service_plan_id = var.service_plan_id

  storage_account_name       = var.storage_account_name
  storage_account_access_key = var.storage_account_access_key

  https_only                      = var.https_only
  builtin_logging_enabled         = var.builtin_logging_enabled
  client_certificate_mode         = var.client_certificate_mode
  ftp_publish_basic_authentication_enabled = false
  webdeploy_publish_basic_authentication_enabled = false

  app_settings = var.app_settings

  site_config {
    application_insights_connection_string = var.application_insights_connection_string

    ftps_state = var.ftps_state

    application_stack {
      python_version = var.python_version
    }

    cors {
      allowed_origins = var.allowed_origins
    }
  }

  tags = var.tags
}