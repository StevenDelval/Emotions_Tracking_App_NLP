terraform {
  required_version = ">= 1.0"


required_providers {
  azurerm ={
    source = "hashicorp/azurerm"
    version = "~>2.0"
  }
}
}

provider "azurerm"{
  features {}
}


resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_kubernetes_cluster" "aks_cluster" {
  name                = var.cluster_name
  kubernetes_version  = var.kubernetes_version
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "AKStest-IA"
  

  default_node_pool {
    name       = "system"
    node_count = var.system_node_count
    vm_size    = "Standard_D2s_v3"

  }

  identity {
    type = "SystemAssigned"
  }

  network_profile {
    load_balancer_sku = "standard"
    network_plugin    = "kubenet" # azure (CNI)
  }
}
