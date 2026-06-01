
# #90DaysOfDevOps - Day 65: 
## Objective

Today I learned how to create reusable Terraform modules, use modules from the Terraform Registry, and deploy multiple EC2 instances using the same custom module.

---

# Task 1: Understand Module Structure

## Terraform Module Directory Structure

```text
terraform-modules/
├── main.tf
├── variables.tf
├── outputs.tf
├── providers.tf
└── modules/
    ├── ec2-instance/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    └── security-group/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
````

## Question & Answer

### Q: What is the difference between a Root Module and a Child Module?

**Answer:**

* Root Module is the main Terraform configuration where execution starts.
* Child Module is a reusable module called by the root module.
* Terraform commands such as `terraform init`, `terraform plan`, and `terraform apply` are executed from the root module.
* Child modules help reduce code duplication and improve reusability.

---

# Task 2: Build a Custom EC2 Module

## variables.tf

```hcl
variable "ami_id" {
  type = string
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "subnet_id" {
  type = string
}

variable "security_group_ids" {
  type = list(string)
}

variable "instance_name" {
  type = string
}

variable "tags" {
  type    = map(string)
  default = {}
}
```

## main.tf

```hcl
resource "aws_instance" "this" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids = var.security_group_ids

  tags = merge(
    {
      Name = var.instance_name
    },
    var.tags
  )
}
```

## outputs.tf

```hcl
output "instance_id" {
  value = aws_instance.this.id
}

output "public_ip" {
  value = aws_instance.this.public_ip
}

output "private_ip" {
  value = aws_instance.this.private_ip
}
```

---

# Task 3: Build a Custom Security Group Module

## What is a Dynamic Block?

A dynamic block allows Terraform to generate multiple nested blocks using a loop.

Example:

```hcl
dynamic "ingress" {
  for_each = var.ingress_ports

  content {
    from_port   = ingress.value
    to_port     = ingress.value
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

If ingress_ports is:

```hcl
[22,80,443]
```

Terraform automatically creates three ingress rules.

---

# Task 4: Call Modules From Root Module

## Root main.tf

```hcl
module "web_sg" {
  source        = "./modules/security-group"
  vpc_id        = module.vpc.vpc_id
  sg_name       = "terraweek-web-sg"
  ingress_ports = [22,80,443]
  tags          = local.common_tags
}

module "web_server" {
  source             = "./modules/ec2-instance"
  ami_id             = data.aws_ami.amazon_linux.id
  instance_type      = "t3.micro"
  subnet_id          = module.vpc.public_subnets[0]
  security_group_ids = [module.web_sg.sg_id]
  instance_name      = "terraweek-web"
  tags               = local.common_tags
}

module "api_server" {
  source             = "./modules/ec2-instance"
  ami_id             = data.aws_ami.amazon_linux.id
  instance_type      = "t3.micro"
  subnet_id          = module.vpc.public_subnets[0]
  security_group_ids = [module.web_sg.sg_id]
  instance_name      = "terraweek-api"
  tags               = local.common_tags
}
```

## Screenshot

* terraweek-web instance
* terraweek-api instance
* Same Security Group attached
* Running state

```text
<img width="1064" height="339" alt="Screenshot 2026-05-31 194843" src="https://github.com/user-attachments/assets/d2e708d8-9827-40eb-a779-df8dcb1a470e" />
<img width="1127" height="286" alt="Screenshot 2026-05-31 193645" src="https://github.com/user-attachments/assets/b3f4ed16-584c-4b23-a1ad-6345f70cec0e" />
<img width="1212" height="750" alt="Screenshot 2026-05-31 193624" src="https://github.com/user-attachments/assets/9fad5d43-4b10-46a7-aabf-a5d43b1971db" />

```

---

# Task 5: Use a Public Registry Module

## Registry VPC Module

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "terraweek-vpc"
  cidr = "10.0.0.0/16"

  azs = [
    "us-east-2a",
    "us-east-2b"
  ]

  public_subnets = [
    "10.0.1.0/24",
    "10.0.2.0/24"
  ]

  private_subnets = [
    "10.0.3.0/24",
    "10.0.4.0/24"
  ]

  enable_nat_gateway   = false
  enable_dns_hostnames = true

  tags = local.common_tags
}
```

## Question & Answer

### Q: Where does Terraform download registry modules?

**Answer:**

Terraform downloads registry modules inside:

```text
.terraform/modules/
```

Example:

```text
.terraform/
└── modules/
    └── vpc/
```

---

# Task 6: Module Versioning

## Version Examples

### Exact Version

```hcl
version = "5.1.0"
```

### Allow Any 5.x Version

```hcl
version = "~> 5.0"
```

### Version Range

```hcl
version = ">= 5.0, < 6.0"
```

## Upgrade Modules

```bash
terraform init -upgrade
```

---

# State File Observation

## Command

```bash
terraform state list
```

## Example Output

```text
module.vpc.aws_vpc.this[0]
module.vpc.aws_subnet.public[0]
module.web_sg.aws_security_group.this
module.web_server.aws_instance.this
module.api_server.aws_instance.this
```

---

# Comparison: Hand-Written VPC vs Registry VPC Module

| Hand-Written VPC                          | Registry VPC Module                                 |
| ----------------------------------------- | --------------------------------------------------- |
| Creates only resources explicitly defined | Creates multiple networking resources automatically |
| More manual work                          | Faster deployment                                   |
| Good for learning                         | Better for production                               |
| Less reusable                             | Highly reusable                                     |
| Around 5 resources                        | Around 10-20+ resources depending on configuration  |

### Hand-Written VPC Resources

* VPC
* Subnet
* Internet Gateway
* Route Table
* Route Table Association

### Registry Module Resources

* VPC
* Public Subnets
* Private Subnets
* Route Tables
* Route Associations
* Internet Gateway
* Default Resources
* DHCP Options
* Additional Networking Components

---

# Five Terraform Module Best Practices

## 1. Always Pin Module Versions

Pin versions to avoid unexpected breaking changes.

## 2. Keep Modules Focused

Each module should handle only one responsibility.

Examples:

* EC2 Module
* VPC Module
* Security Group Module

## 3. Use Variables Instead of Hardcoding

This makes modules reusable across environments.

## 4. Always Define Outputs

Outputs allow other modules and root modules to consume resource information.

## 5. Add a README.md

Every module should include documentation for:

* Inputs
* Outputs
* Usage Examples
* Requirements

---

# Commands Used

```bash
terraform init
terraform plan
terraform apply
terraform state list
terraform init -upgrade
terraform destroy
```

---

# Key Learnings

* Built reusable Terraform modules.
* Created custom EC2 and Security Group modules.
* Used dynamic blocks for ingress rules.
* Reused a single module to deploy multiple EC2 instances.
* Used a Terraform Registry module.
* Learned module versioning strategies.
* Explored Terraform state entries for modules.
* Understood Terraform module best practice.
