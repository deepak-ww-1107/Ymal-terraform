variable "name" {}
variable "location" {}
variable "resource_group_name" {}
variable "custom_subdomain_name" {}
variable "sku_name" {}
variable "identity_type" {}
variable "default_action" {}
variable "ip_rules" {
  type = list(string)
}
variable "tags" {
  type = map(string)
}