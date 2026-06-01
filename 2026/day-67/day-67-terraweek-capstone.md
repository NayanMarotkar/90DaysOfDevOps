
# #90DaysOfDevOps - Day 67: Terraform Capstone Project (Multi-Environment Infrastructure)

## Objective

Today I completed a Terraform Capstone Project that combines everything learned throughout TerraWeek. I built reusable Terraform modules, implemented environment isolation using Terraform Workspaces, deployed separate Dev, Staging, and Production environments, and followed Infrastructure as Code best practices.

This project demonstrates how real-world organizations manage multiple environments using a single Terraform codebase.

---

# Project Structure

```text
terraweek-capstone/
├── providers.tf
├── variables.tf
├── outputs.tf
├── locals.tf
├── main.tf
├── dev.tfvars
├── staging.tfvars
├── prod.tfvars
├── .gitignore
│
└── modules/
    ├── vpc/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    │
    ├── security-group/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    │
    └── ec2-instance/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
````

---

# Task 1: Learn Terraform Workspaces

## Commands Used

```bash
terraform workspace show

terraform workspace new dev
terraform workspace new staging
terraform workspace new prod

terraform workspace list

terraform workspace select dev
terraform workspace select staging
terraform workspace select prod
```

## Questions and Answers

### Q1. What does terraform.workspace return inside a configuration?

**Answer:**

terraform.workspace returns the currently selected workspace name.

Examples:

```text
dev
staging
prod
```

This allows infrastructure behavior to change automatically depending on the selected workspace.

---

### Q2. Where does each workspace store its state file?

**Answer:**

Default workspace:

```text
terraform.tfstate
```

Additional workspaces:

```text
terraform.tfstate.d/
├── dev/
│   └── terraform.tfstate
├── staging/
│   └── terraform.tfstate
└── prod/
    └── terraform.tfstate
```

Each workspace maintains its own isolated Terraform state.

---

### Q3. How is this different from using separate directories?

**Answer:**

#### Workspaces

* Single codebase
* Multiple state files
* Easy environment switching
* Less duplication

#### Separate Directories

* Separate Terraform code per environment
* Separate state per directory
* More flexibility
* More maintenance effort

Workspaces are useful when environments are mostly identical.

---

# Task 2: Project Setup

## .gitignore

```gitignore
.terraform/
*.tfstate
*.tfstate.backup
*.tfvars
.terraform.lock.hcl
```

### Q. Why is this file structure considered best practice?

**Answer:**

* Separates configuration by purpose.
* Improves readability.
* Makes troubleshooting easier.
* Encourages reusable modules.
* Supports team collaboration.
* Reduces code duplication.
* Scales easily for large projects.
* Follows Infrastructure as Code standards.

---

# Task 3: Custom Modules

## Module 1: VPC Module

### modules/vpc/variables.tf

```hcl
variable "cidr" {}
variable "public_subnet_cidr" {}
variable "environment" {}
variable "project_name" {}
```

### modules/vpc/main.tf

```hcl
resource "aws_vpc" "this" {
  cidr_block = var.cidr

  tags = {
    Name        = "${var.project_name}-${var.environment}-vpc"
    Environment = var.environment
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.this.id
  cidr_block              = var.public_subnet_cidr
  map_public_ip_on_launch = true
}

resource "aws_internet_gateway" "this" {
  vpc_id = aws_vpc.this.id
}
```

### modules/vpc/outputs.tf

```hcl
output "vpc_id" {
  value = aws_vpc.this.id
}

output "subnet_id" {
  value = aws_subnet.public.id
}
```

---

## Module 2: Security Group Module

### modules/security-group/variables.tf

```hcl
variable "vpc_id" {}
variable "ingress_ports" {}
variable "environment" {}
variable "project_name" {}
```

### modules/security-group/main.tf

```hcl
resource "aws_security_group" "this" {
  vpc_id = var.vpc_id

  dynamic "ingress" {
    for_each = var.ingress_ports

    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

### modules/security-group/outputs.tf

```hcl
output "sg_id" {
  value = aws_security_group.this.id
}
```

---

## Module 3: EC2 Instance Module

### modules/ec2-instance/variables.tf

```hcl
variable "ami_id" {}
variable "instance_type" {}
variable "subnet_id" {}
variable "security_group_ids" {}
variable "environment" {}
variable "project_name" {}
```

### modules/ec2-instance/main.tf

```hcl
resource "aws_instance" "this" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids = var.security_group_ids

  tags = {
    Name = "${var.project_name}-${var.environment}-server"
  }
}
```

### modules/ec2-instance/outputs.tf

```hcl
output "instance_id" {
  value = aws_instance.this.id
}

output "public_ip" {
  value = aws_instance.this.public_ip
}
```

---

# Task 4: Workspace-Aware Configuration

## locals.tf

```hcl
locals {
  environment = terraform.workspace

  name_prefix = "${var.project_name}-${local.environment}"

  common_tags = {
    Project     = var.project_name
    Environment = local.environment
    ManagedBy   = "Terraform"
    Workspace   = terraform.workspace
  }
}
```

## Root main.tf

```hcl
module "vpc" {
  source             = "./modules/vpc"
  cidr               = var.vpc_cidr
  public_subnet_cidr = var.subnet_cidr
  environment        = local.environment
  project_name       = var.project_name
}

module "security_group" {
  source        = "./modules/security-group"
  vpc_id        = module.vpc.vpc_id
  ingress_ports = var.ingress_ports
  environment   = local.environment
  project_name  = var.project_name
}

module "server" {
  source             = "./modules/ec2-instance"
  ami_id             = data.aws_ami.amazon_linux.id
  instance_type      = var.instance_type
  subnet_id          = module.vpc.subnet_id
  security_group_ids = [module.security_group.sg_id]
  environment        = local.environment
  project_name       = var.project_name
}
```

---

# Environment-Specific tfvars Files

## dev.tfvars

```hcl
vpc_cidr      = "10.0.0.0/16"
subnet_cidr   = "10.0.1.0/24"
instance_type = "t3.micro"
ingress_ports = [22, 80]
```

### Dev Highlights

* SSH Enabled
* Smallest Instance
* Development Testing

---

## staging.tfvars

```hcl
vpc_cidr      = "10.1.0.0/16"
subnet_cidr   = "10.1.1.0/24"
instance_type = "t3.small"
ingress_ports = [22, 80, 443]
```

### Staging Highlights

* SSH Enabled
* HTTPS Enabled
* Pre-production Testing

---

## prod.tfvars

```hcl
vpc_cidr      = "10.2.0.0/16"
subnet_cidr   = "10.2.1.0/24"
instance_type = "t3.small"
ingress_ports = [80, 443]
```

### Production Highlights

* No SSH Access
* HTTP + HTTPS Only
* Production Environment

---

# Task 5: Deploy All Three Environments

## Deployment Commands

```bash
terraform workspace select dev
terraform apply -var-file="dev.tfvars"

terraform workspace select staging
terraform apply -var-file="staging.tfvars"

terraform workspace select prod
terraform apply -var-file="prod.tfvars"
```

## Verification

### AWS Console Verification

Verified:

* Three independent VPCs
* Three independent subnets
* Three independent security groups
* Three EC2 instances
* Different CIDR ranges
* Different security rules
* Different Name tags

### Screenshot

```text
[Screenshot: Dev, Staging, and Prod environments running simultaneously]
```

---

### Terraform Output Screenshots

```text
[Screenshot: terraform output from dev workspace]
```

```text
[Screenshot: terraform output from staging workspace]
```

```text
[Screenshot: terraform output from prod workspace]
```

### Q. Are all three environments completely isolated?

**Answer:**

Yes.

Each environment has:

* Separate state file
* Separate VPC
* Separate subnet
* Separate security group
* Separate EC2 instance
* Separate CIDR range

Changes in one environment do not impact the others.

---

# Task 6: Terraform Best Practices Guide

## File Structure

* Separate providers.tf
* Separate variables.tf
* Separate outputs.tf
* Separate locals.tf
* Separate main.tf

## State Management

* Use remote backends
* Enable state locking
* Enable versioning
* Protect state files

## Variables

* Never hardcode values
* Use tfvars files
* Add validation blocks
* Keep sensible defaults

## Modules

* One responsibility per module
* Always define variables
* Always define outputs
* Pin registry module versions

## Workspaces

* Use for environment isolation
* Use terraform.workspace
* Keep state separated

## Security

* Ignore state files in Git
* Ignore tfvars files
* Encrypt state storage
* Restrict backend access

## Commands

Always run:

```bash
terraform fmt
terraform validate
terraform plan
```

before:

```bash
terraform apply
```

## Tagging

Tag every resource with:

* Project
* Environment
* ManagedBy
* Workspace

## Naming Convention

```text
<project>-<environment>-<resource>
```

Example:

```text
terraweek-dev-server
terraweek-staging-server
terraweek-prod-server
```

## Cleanup

Destroy unused environments:

```bash
terraform destroy
```

to avoid cloud costs.

---

# Task 7: Destroy All Environments

```bash
terraform workspace select prod
terraform destroy -var-file="prod.tfvars"

terraform workspace select staging
terraform destroy -var-file="staging.tfvars"

terraform workspace select dev
terraform destroy -var-file="dev.tfvars"
```

## Delete Workspaces

```bash
terraform workspace select default

terraform workspace delete dev
terraform workspace delete staging
terraform workspace delete prod
```

### Verification

Verified:

* No EC2 instances
* No VPCs
* No Security Groups
* No Internet Gateways
* No Subnets

AWS account completely cleaned up.

---

# TerraWeek Learning Journey

| Day | Concepts Learned                                                      |
| --- | --------------------------------------------------------------------- |
| 61  | IaC, HCL, init, plan, apply, destroy, state basics                    |
| 62  | Providers, resources, dependencies, lifecycle                         |
| 63  | Variables, outputs, data sources, locals, functions                   |
| 64  | Remote backend, locking, import, drift detection                      |
| 65  | Custom modules, registry modules, versioning                          |
| 66  | Amazon EKS, managed node groups, real-world provisioning              |
| 67  | Terraform Workspaces, multi-environment deployments, capstone project |

---

# Key Learnings

* Built reusable Terraform modules.
* Used Terraform Workspaces for environment isolation.
* Managed Dev, Staging, and Production from a single codebase.
* Applied Infrastructure as Code best practices.
* Improved project organization.
* Learned state isolation strategies.
* Applied real-world naming conventions.
* Practiced complete infrastructure lifecycle management.
* Successfully completed the Terraform TerraWeek Capstone Project.
