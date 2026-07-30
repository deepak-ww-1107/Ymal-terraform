resource "azurerm_search_service" "this" {
  name                       = var.name
  location                   = var.location
  resource_group_name        = var.resource_group_name
  sku                        = var.sku
  semantic_search_sku        = var.semantic_search_sku
  network_rule_bypass_option = var.network_rule_bypass_option
  tags                       = var.tags
}