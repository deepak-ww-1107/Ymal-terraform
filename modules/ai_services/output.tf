output "id" {
  value = azurerm_ai_services.this.id
}

output "name" {
  value = azurerm_ai_services.this.name
}

output "principal_id" {
  value = azurerm_ai_services.this.identity[0].principal_id
}