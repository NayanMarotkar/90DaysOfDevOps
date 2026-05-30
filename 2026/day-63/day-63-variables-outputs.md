# Day 63: Terraform Variables, Outputs, Locals & Data Sources


2. Variable Precedence (Lowest to Highest)

Default values in variables.tf
Environment Variables (TF_VAR_*)
terraform.tfvars
*.auto.tfvars
-var-file flag
-var flag (Highest)

Example:
Bashterraform plan -var-file="prod.tfvars" -var="instance_type=t2.nano"

3. Five Most Useful Built-in Functions

merge() - Combines maps (used for tags)
format() - String formatting
lookup() - Safe map lookup with default
cidrsubnet() - Calculate subnets dynamically
upper() / lower() - Case conversion

4. Difference Between Variable, Local, Output, and Data

Variable → Input from user / tfvars (customizable)
Local → Internal computed values (like variables but calculated inside config)
O
utput → Values returned after apply (for display or chaining)
Data Source → Read existing data from AWS (e.g., latest AMI)

## 5. `variables.tf` (All Variable Types)

```hcl
variable "region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-2"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "subnet_cidr" {
  description = "CIDR block for Public Subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "availability_zone" {
  description = "Availability Zone"
  type        = string
  default     = "us-east-2b"
}

variable "instance_type" {
  description = "EC2 Instance Type"
  type        = string
  default     = "t3.micro"
}

variable "project_name" {
  description = "Project Name (Required)"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "allowed_ports" {
  description = "List of allowed inbound ports"
  type        = list(number)
  default     = [22, 80, 443]
}

variable "extra_tags" {
  description = "Additional tags"
  type        = map(string)
  default     = {}
}

2. Variable Files

terraform.tfvars
hclproject_name  = "terraweek"
environment   = "dev"
instance_type = "t2.micro"

prod.tfvars
hclproject_name = "terraweek"
environment  = "prod"
instance_type = "t3.small"
vpc_cidr     = "10.1.0.0/16"
subnet_cidr  = "10.1.1.0/24"
