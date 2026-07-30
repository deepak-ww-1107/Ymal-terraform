variable "name" {}
variable "location" {}
variable "resource_group_name" {}
variable "custom_subdomain_name" {}
variable "kind" {}
variable "sku_name" {}
variable "identity_type" {}
variable "default_action" {}
variable "tags" {
  type = map(string)
}