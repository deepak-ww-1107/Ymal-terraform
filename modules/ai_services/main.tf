resource "azurerm_ai_services" "this" {
  name                  = var.name
  location              = var.location
  resource_group_name   = var.resource_group_name
  custom_subdomain_name = var.custom_subdomain_name
  sku_name              = var.sku_name
  tags                  = var.tags

  identity {
    type = var.identity_type
  }

  network_acls {
    default_action = var.default_action
    ip_rules       = var.ip_rules
  }
}