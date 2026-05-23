
# Day 61: Terraform Introduction

## Infrastructure as Code (IaC)

Infrastructure as Code (IaC) is the practice of managing and provisioning infrastructure using code instead of manually clicking in the AWS console. Instead of creating servers, buckets, or networks by hand, you write configuration files that describe what you want. Terraform then automatically creates and manages these resources. 

IaC makes infrastructure repeatable, version-controlled, and consistent across environments. It is a core part of DevOps because it enables faster deployments, reduces human errors, and allows teams to collaborate better using Git.

## Terraform Resources Created

**Screenshots:**

1. **Terraform Apply Output** (S3 Bucket + EC2 Instance)
   <img width="1880" height="799" alt="Screenshot 2026-05-23 195131" src="https://github.com/user-attachments/assets/385d7c20-d8c8-4e02-bf47-44aa85b979bd" />
   <img width="1542" height="424" alt="Screenshot 2026-05-23 200153" src="https://github.com/user-attachments/assets/8615179f-b014-4d03-bc23-e994870b4ea7" />


2. **AWS Console - Resources**
   - **S3 Bucket**: `nayan-terraform-basics-bucket-2026`
   - **EC2 Instance**: `TerraWeek-Day1` (t2.micro)

   <img width="1542" height="424" alt="Screenshot 2026-05-23 200153" src="https://github.com/user-attachments/assets/db59f43a-b8c8-4a1e-b132-39cd1f976608" />
   <img width="1451" height="424" alt="Screenshot 2026-05-23 195209" src="https://github.com/user-attachments/assets/ce731030-3e03-4699-85f9-6c2236003143" />


## Terraform Commands

| Command                  | What it does |
|-------------------------|--------------|
| `terraform init`        | Initializes the working directory, downloads required providers, and creates `.terraform` folder and lock file. |
| `terraform plan`        | Shows what changes Terraform will make (create, update, or destroy) without actually doing it. |
| `terraform apply`       | Creates or updates resources to match the configuration. Requires confirmation (`yes`). |
| `terraform destroy`     | Destroys all resources managed by Terraform. |
| `terraform show`        | Displays the current state in a human-readable format. |
| `terraform state list`  | Lists all resources currently tracked in the state file. |

## Terraform State File

The **terraform.tfstate** file is a JSON file that Terraform uses to track all the resources it manages.

**What it contains:**
- Resource IDs
- All attributes of resources (ARN, IP address, tags, etc.)
- Resource dependencies
- Current configuration mapping

**Why it matters:**
- Helps Terraform know what already exists
- Enables it to calculate only the necessary changes
- Makes Terraform **idempotent** (running apply multiple times gives same result)

> **Never manually edit** the state file and **do not commit** it to Git.

## All Task Questions & Answers

### Task 1: IaC Basics

**1. What is IaC? Why does it matter in DevOps?**  
IaC means writing infrastructure as code. It matters in DevOps because it brings speed, consistency, automation, and collaboration between Dev and Ops teams.

**2. What problems does IaC solve?**  
It solves manual errors, inconsistency between environments, difficulty in reproducing setups, and lack of version control.

**3. How is Terraform different from others?**  
- Terraform: Declarative, cloud-agnostic  
- CloudFormation: AWS-only  
- Ansible: More for configuration management  
- Pulumi: Uses real programming languages

**4. What does declarative and cloud-agnostic mean?**  
Declarative = You say *what* you want, not *how*.  
Cloud-agnostic = Works with AWS, Azure, GCP, etc. using same code style.

### Task 3: S3 Bucket + EC2

**What did `terraform init` download?**  
It downloaded the AWS provider plugin.

**What does `.terraform/` directory contain?**  
It contains downloaded providers and the `.terraform.lock.hcl` file.

### Task 5: State File

**What information does the state file store?**  
It stores current real-world details of all resources (IDs, attributes, metadata).

**Why should you never manually edit the state file?**  
It can corrupt the state and cause Terraform to lose track of resources.

**Why should the state file not be committed to Git?**  
It may contain sensitive data, is environment-specific, and can cause merge conflicts.
