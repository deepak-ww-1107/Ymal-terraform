variable "name" {}
variable "location" {}
variable "resource_group_name" {}

variable "service_plan_id" {}
variable "storage_account_name" {}
variable "storage_account_access_key" {}

variable "application_insights_connection_string" {}

variable "identity_type" {
  default = "SystemAssigned"
}

variable "https_only" {
  default = true
}

variable "public_network_access_enabled" {
  default = false
}

variable "builtin_logging_enabled" {
  default = false
}

variable "client_certificate_mode" {
  default = "Optional"
}

variable "ftp_publish_basic_authentication_enabled" {
  default = false
}

variable "webdeploy_publish_basic_authentication_enabled" {
  default = false
}

variable "auth_enabled" {
  default = false
}

variable "token_refresh_extension_hours" {
  default = 0
}

variable "http2_enabled" {
  default = true
}

variable "vnet_route_all_enabled" {
  default = true
}

variable "ftps_state" {
  default = "Disabled"
}

variable "ip_restriction_default_action" {
  default = "Allow"
}

variable "allowed_origins" {
  type    = list(string)
  default = []
}

variable "app_settings" {
  type = map(string)
}

variable "tags" {
  type = map(string)
}

variable "ip_restrictions" {
  type = list(object({
    ip_address = string
    action      = string
    priority    = number
    name        = string
  }))
  default = []
}