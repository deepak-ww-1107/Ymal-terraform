variable "name" {
  type = string
}

variable "location" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "service_plan_id" {
  type = string
}

variable "storage_account_name" {
  type = string
}

variable "storage_account_access_key" {
  type      = string
  sensitive = true
}

variable "https_only" {
  type = bool
}

variable "builtin_logging_enabled" {
  type = bool
}

variable "client_certificate_mode" {
  type = string
}

variable "application_insights_connection_string" {
  type = string
}

variable "ftps_state" {
  type = string
}

variable "python_version" {
  type = string
}

variable "allowed_origins" {
  type = list(string)
}

variable "app_settings" {
  type = map(string)
}

variable "tags" {
  type = map(string)
}

# variable "auth_secret" {
#   type      = string
#   sensitive = true
# }

variable "public_network_access_enabled" {
  type = bool
  default = true
}

variable "virtual_network_subnet_id" {
  type = string
  default = null
}

variable "application_insights_key" {
  type = string
  default = null
}

variable "http2_enabled" {
  type = bool
  default = false
}

variable "vnet_route_all_enabled" {
  type = bool
  default = false
}

variable "identity_type" {
  type = string
  default = "SystemAssigned"
}