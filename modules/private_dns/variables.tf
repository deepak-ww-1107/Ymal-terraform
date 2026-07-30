variable "resource_group_name" {
  type = string
}

variable "virtual_network_id" {
  type = string
}

variable "private_dns_zone_names" {
  type = map(string)
}

variable "registration_enabled" {
  type    = bool
  default = false
}

variable "tags" {
  type = map(string)
}