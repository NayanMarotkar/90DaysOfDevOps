
# Day 62: Terraform AWS Infrastructure - Providers & Resources

## Project Overview
This document contains the complete Terraform configuration for creating VPC, Subnet, IGW, Route Table, Security Group, EC2 Instance, and S3 Bucket.


Screenshot -
<img width="1344" height="777" alt="Screenshot 2026-05-30 111035" src="https://github.com/user-attachments/assets/b9d15e65-138c-4f71-a6b2-cb64234dd2e6" />
<img width="1497" height="790" alt="Screenshot 2026-05-30 111322" src="https://github.com/user-attachments/assets/da0ec889-5f35-4710-aa7a-f1d5c2877711" />
<img width="1334" height="760" alt="Screenshot 2026-05-30 112728" src="https://github.com/user-attachments/assets/a9cea73d-a400-4c94-9a25-870f1c25c014" />
<img width="1565" height="323" alt="Screenshot 2026-05-30 114438" src="https://github.com/user-attachments/assets/df1af099-03c8-4c52-99b2-770df888817d" />
<img width="1570" height="697" alt="Screenshot 2026-05-30 114643" src="https://github.com/user-attachments/assets/43a29833-40e2-4cf5-a561-d9d390bd1184" />

aws_vpc.my_vpc
├── aws_subnet.public
├── aws_internet_gateway.igw → aws_route_table.public → aws_route_table_association.public
├── aws_security_group.web_sg
└── aws_instance.web_server → aws_s3_bucket.logs (explicit)


Implicit vs Explicit Dependencies
Implicit: Terraform auto-detects via references like vpc_id = aws_vpc.my_vpc.id.
Explicit: Manually added using depends_on = [...] when no direct reference exists (used for S3 bucket after EC2).
---

## Full `main.tf` with Comments

```hcl
#VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"

    tags = {
      Name = "TerraWeek-VPC"
    }
}

#Public Subnet
resource "aws_subnet" "Public" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone = "us-east-2b"

  tags = {
    Name = "TerraWeek-Public-Subnet"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.my_vpc.id

  tags = {
    Name = "TerraWeek-IGW"
  }
}

# Route Table
resource "aws_route_table" "Public" {
    vpc_id = aws_vpc.my_vpc.id

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.igw.id
    }

    tags = {
      Name = "TerraWeek-Public-RT"
    }
  
}

#Route Table Association
resource "aws_route_table_association" "Public" {
    subnet_id = aws_subnet.Public.id
    route_table_id = aws_route_table.Public.id
  
}

# Security Group
resource "aws_security_group" "web_sg" {
  name        = "TerraWeek-SG"
  description = "Allow SSH and HTTP inbound traffic"
  vpc_id      = aws_vpc.my_vpc.id

  # SSH Access
  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTP Access
  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "TerraWeek-SG"
  }
}

# EC2 Instance
resource "aws_instance" "web_server" {
  ami                         = "ami-078f95be0757084a3"
  instance_type               = "t3.micro"
  subnet_id                   = aws_subnet.Public.id
  vpc_security_group_ids      = [aws_security_group.web_sg.id]
  associate_public_ip_address = true

  tags = {
    Name = "TerraWeek-Server"
  }

  # Lifecycle Rule
  lifecycle {
    create_before_destroy = true
  }
}

# Output the Public IP
output "instance_public_ip" {
  value = aws_instance.web_server.public_ip
}

# Random string for unique S3 bucket name
resource "random_string" "suffix" {
  length  = 8
  special = false
  upper   = false
}

# S3 Bucket for Application Logs
resource "aws_s3_bucket" "logs" {
  bucket = "terraweek-app-logs-${random_string.suffix.result}"

  tags = {
    Name        = "TerraWeek-App-Logs"
    Environment = "Terraform-Demo"
  }

  # Explicit dependency: Create S3 bucket only AFTER EC2 instance
  depends_on = [aws_instance.web_server]
}

----
