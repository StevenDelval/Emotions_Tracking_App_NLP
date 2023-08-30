variable "resource_group_name" {
  description = "ressource-group"
  default = "AKStest-IA"
}

variable "location" {
  description = "location"
  default = "north europe"
}

variable "cluster_name" {
  description = "cluster name"
  default = "AKStest-IA"
}

variable "kubernetes_version" {
  description = "version"
  default = "1.27.3"
}

variable "system_node_count" {
  description = "noeuds"
  default = "3"
}