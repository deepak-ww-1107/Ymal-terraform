resource "azurerm_monitor_smart_detector_alert_rule" "this" {
  name                = var.name
  resource_group_name = var.resource_group_name
  scope_resource_ids  = var.scope_resource_ids
  detector_type       = var.detector_type
  severity            = var.severity
  frequency           = var.frequency
  description         = var.description
  tags = var.tags

  action_group {
    ids = var.action_group_ids
  }
}