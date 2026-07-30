variable "name" {
  type = string
}

variable "location" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "subnet_id" {
  type = string
}

variable "private_dns_zone_group_name" {
  type    = string
  default = "default"
}

variable "private_dns_zone_ids" {
  type = list(string)
}

variable "private_service_connection_name" {
  type = string
}

variable "private_connection_resource_id" {
  type = string
}

variable "subresource_names" {
  type = list(string)
}

variable "is_manual_connection" {
  type    = bool
  default = false
}

variable "tags" {
  type    = map(string)
  default = {}
}