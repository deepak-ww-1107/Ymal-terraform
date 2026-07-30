resource "azurerm_storage_account" "this" {
  name                            = var.name
  location                        = var.location
  resource_group_name             = var.resource_group_name
  account_tier                    = var.account_tier
  account_replication_type        = var.account_replication_type
  account_kind                    = var.account_kind
  allow_nested_items_to_be_public = var.allow_nested_items_to_be_public
  default_to_oauth_authentication = var.default_to_oauth_authentication
  public_network_access_enabled = var.public_network_access_enabled
  tags = var.tags
}