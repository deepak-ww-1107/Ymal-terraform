resource "azurerm_windows_function_app" "this" {
  name                = var.name
  location            = var.location
  resource_group_name = var.resource_group_name

  service_plan_id = var.service_plan_id

  storage_account_name       = var.storage_account_name
  storage_account_access_key = var.storage_account_access_key

  builtin_logging_enabled                  = var.builtin_logging_enabled
  client_certificate_mode                  = var.client_certificate_mode
  ftp_publish_basic_authentication_enabled = false
  webdeploy_publish_basic_authentication_enabled = false

  app_settings = var.app_settings
  tags         = var.tags

  site_config {
    application_insights_connection_string = var.application_insights_connection_string
    ftps_state                             = var.ftps_state
    ip_restriction_default_action          = var.ip_restriction_default_action

    cors {
      allowed_origins = var.allowed_origins
    }
  }
}