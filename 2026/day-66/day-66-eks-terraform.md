# #90DaysOfDevOps - Day 66: Provisioning Amazon EKS with Terraform

## Objective

Today I learned how to provision a production-grade Kubernetes cluster on AWS using Terraform and the official Terraform Registry modules. I created a custom VPC, deployed an Amazon EKS cluster with managed node groups, connected kubectl to the cluster, deployed an Nginx application, and finally cleaned up all resources to avoid unnecessary AWS charges.

---

# Task 1: Project Setup

## Project Structure

```text
terraform-eks/
├── providers.tf
├── variables.tf
├── terraform.tfvars
├── vpc.tf
├── eks.tf
├── outputs.tf
└── k8s/
    └── nginx-deployment.yaml
````

## providers.tf

```hcl
terraform {
  required_version = ">= 1.5"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.30"
    }
  }
}

provider "aws" {
  region = var.region
}
```

## variables.tf

```hcl
variable "region" {
  type    = string
  default = "us-east-2"
}

variable "cluster_name" {
  type    = string
  default = "terraweek-eks"
}

variable "cluster_version" {
  type    = string
  default = "1.31"
}

variable "node_instance_type" {
  type    = string
  default = "t3.small"
}

variable "node_desired_count" {
  type    = number
  default = 2
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}
```

---

# Task 2: Create the VPC with Registry Module

## VPC Module Configuration

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "terraweek-vpc"
  cidr = var.vpc_cidr

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

  enable_nat_gateway   = true
  single_nat_gateway   = true
  enable_dns_hostnames = true

  public_subnet_tags = {
    "kubernetes.io/role/elb" = 1
  }

  private_subnet_tags = {
    "kubernetes.io/role/internal-elb" = 1
  }
}
```

## Question & Answer

### Q: Why does EKS require both public and private subnets?

**Answer:**

Public subnets are used for internet-facing Load Balancers that expose applications to external users.

Private subnets are used for worker nodes to improve security. The worker nodes are not directly accessible from the internet and use a NAT Gateway for outbound connectivity.

### Q: What do the subnet tags do?

**Answer:**

```text
kubernetes.io/role/elb
```

Allows Kubernetes to place public AWS Load Balancers in public subnets.

```text
kubernetes.io/role/internal-elb
```

Allows Kubernetes to place internal AWS Load Balancers in private subnets.

These tags help Kubernetes automatically discover suitable subnets.

---

# Task 3: Create the EKS Cluster with Registry Module

## EKS Module Configuration

```hcl
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = var.cluster_name
  cluster_version = var.cluster_version

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  cluster_endpoint_public_access = true

  eks_managed_node_groups = {
    terraweek_nodes = {
      ami_type       = "AL2_x86_64"
      instance_types = [var.node_instance_type]

      min_size     = 1
      max_size     = 3
      desired_size = var.node_desired_count
    }
  }

  tags = {
    Environment = "dev"
    Project     = "TerraWeek"
    ManagedBy   = "Terraform"
  }
}
```

## Resources Created

Terraform created resources such as:

* VPC
* Public Subnets
* Private Subnets
* Internet Gateway
* NAT Gateway
* Route Tables
* Security Groups
* IAM Roles
* EKS Control Plane
* EKS Managed Node Group
* Launch Templates
* Auto Scaling Groups

### Total Resources Created

```text
[Add the final resource count from terraform apply output]
```

---

# Task 4: Apply and Connect kubectl

## Terraform Apply

```bash
terraform apply
```

### Screenshot

```text
[Screenshot: Terraform Apply Completed Successfully]
```

## Configure kubectl

```bash
aws eks update-kubeconfig \
  --name terraweek-eks \
  --region us-east-2
```

## Verification Commands

```bash
kubectl get nodes
kubectl get pods -A
kubectl cluster-info
```

### Screenshot

```text
[Screenshot: kubectl get nodes showing 2 Ready worker nodes]
```

---

# Task 5: Deploy a Workload on the Cluster

## Nginx Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-terraweek
spec:
  replicas: 3
```

## Deploy

```bash
kubectl apply -f k8s/nginx-deployment.yaml
```

## Verify

```bash
kubectl get deployments
kubectl get pods
kubectl get svc
```

## Load Balancer Service

The Kubernetes Service of type LoadBalancer automatically created an AWS Elastic Load Balancer.

### Screenshot

```text
[Screenshot: Nginx running successfully on EKS]
```

### Verification

Successfully accessed the Nginx Welcome Page through the AWS Load Balancer URL.

---

# Task 6: Destroy Everything

## Remove Kubernetes Resources

```bash
kubectl delete -f k8s/nginx-deployment.yaml
```

This removes:

* Nginx Pods
* Deployment
* Service
* AWS Load Balancer

## Destroy Terraform Infrastructure

```bash
terraform destroy
```

## Verification Checklist

### EKS

```text
No EKS clusters remaining
```

### EC2

```text
No worker nodes running
```

### VPC

```text
TerraWeek VPC deleted
```

### NAT Gateway

```text
Deleted
```

### Elastic IP

```text
Released
```

### Load Balancer

```text
Deleted
```

### Final Verification

AWS account completely cleaned up with no leftover billable resources.

---

# Reflection: EKS vs Kind/Minikube

| Kind / Minikube        | Amazon EKS                           |
| ---------------------- | ------------------------------------ |
| Runs locally           | Runs on AWS                          |
| Single machine cluster | Highly available managed cluster     |
| Good for learning      | Production-ready                     |
| Limited scalability    | Auto-scaling support                 |
| No cloud integrations  | Integrated with IAM, ELB, CloudWatch |
| Quick setup            | Longer provisioning time             |
| Free                   | AWS costs apply                      |

## My Learning

When I created a local Kubernetes cluster using Kind on Day 50, the focus was understanding Kubernetes architecture, pods, services, deployments, and namespaces.

With Amazon EKS, I learned how real-world production Kubernetes clusters are provisioned and managed. Terraform automated the entire infrastructure creation process, including networking, IAM roles, security groups, managed node groups, and the Kubernetes control plane.

This exercise provided valuable hands-on experience with Infrastructure as Code (IaC), managed Kubernetes services, and cloud-native deployments.

---

# Commands Used

```bash
terraform init
terraform plan
terraform apply

aws eks update-kubeconfig \
  --name terraweek-eks \
  --region us-east-2

kubectl get nodes
kubectl get pods -A
kubectl cluster-info

kubectl apply -f k8s/nginx-deployment.yaml

kubectl get deployments
kubectl get pods
kubectl get svc

kubectl delete -f k8s/nginx-deployment.yaml

terraform destroy
```

---

# Key Learnings

* Provisioned Amazon EKS using Terraform.
* Used Terraform Registry modules for VPC and EKS.
* Created public and private subnets for Kubernetes workloads.
* Configured managed node groups.
* Connected kubectl to a managed Kubernetes cluster.
* Deployed and exposed an Nginx application using a LoadBalancer.
* Learned how EKS integrates with AWS networking and IAM.
* Practiced complete infrastructure lifecycle management using Terraform.
* Destroyed all resources to avoid unnecessary AWS costs.
