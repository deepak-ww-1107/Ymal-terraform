variable "name" {}
variable "location" {}
variable "resource_group_name" {}
variable "sku" {}
variable "semantic_search_sku" {}
variable "network_rule_bypass_option" {}
variable "tags" {
  type = map(string)
}