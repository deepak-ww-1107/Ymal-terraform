variable "name" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "short_name" {
  type = string
}

variable "tags" {
  type    = map(string)
  default = {}
}

variable "arm_role_receivers" {
  type = list(object({
    name                    = string
    role_id                 = string
    use_common_alert_schema = bool
  }))
  default = []
}