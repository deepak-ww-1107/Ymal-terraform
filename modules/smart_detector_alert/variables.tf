variable "name" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "scope_resource_ids" {
  type = list(string)
}

variable "action_group_ids" {
  type = list(string)
}

variable "description" {
  type = string
}

variable "detector_type" {
  type = string
}

variable "severity" {
  type = string
}

variable "frequency" {
  type = string
}

variable "tags" {
  type = map(string)
  default = {}
}