resource "azurerm_app_service_certificate" "this" {
  name                = var.name
  location            = var.location
  resource_group_name = var.resource_group_name
}