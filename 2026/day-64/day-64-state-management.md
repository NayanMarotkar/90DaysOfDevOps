# Day 64: Terraform State Management

## 1. Local State vs Remote State Diagram

### Local State
Terraform Config (.tf files)
↓
terraform.tfstate (Local File)
↓
AWS Resources
text**Problems**: No locking, risk of deletion, hard for team collaboration.

### Remote State (S3 + DynamoDB)
Terraform Config (.tf files)
↓
S3 Backend (Encrypted + Versioned)
↓
DynamoDB (State Locking)
↓
AWS Resources
text**Benefits**: Secure, collaborative, versioned, locked.

---

## 2. Screenshots

<img width="1463" height="467" alt="image" src="https://github.com/user-attachments/assets/e15186ff-f21f-4a2b-b847-29ab9ba48cb2" />

*(Screenshot of `dev/terraform.tfstate` inside your S3 bucket `terraweek-state-nayan`)*

<img width="1320" height="707" alt="Screenshot 2026-05-31 183721" src="https://github.com/user-attachments/assets/50fccef4-dc07-4d85-a320-48009cdf1dbf" />

*(Screenshot of lock error when running terraform plan/apply in second terminal)*

---

## 3. Terraform Import Steps & Result

**Steps Followed:**
1. Manually created S3 bucket `terraweek-import-test-nayan` in AWS Console.
2. Added the following block in `main.tf`:
   ```hcl
   resource "aws_s3_bucket" "logs_bucket" {
     bucket = "terraweek-import-test-nayan"
   }

Imported the resource:Bashterraform import aws_s3_bucket.logs_bucket terraweek-import-test-nayan
Ran terraform plan and fixed configuration (tags, etc.).
Final Result: Resource successfully imported and managed by Terraform.


4. State Drift Explanation (Real Example)
I applied my full configuration, then manually changed the Name tag of the EC2 instance to "ManuallyChanged" in the AWS Console.
When I ran terraform plan, Terraform detected the drift and showed that it wanted to update the tag back to the value defined in code.
I ran terraform apply to reconcile the drift. After that, terraform plan showed No changes.

5. Questions & Answers
Q1. What is the difference between terraform import and creating a resource from scratch?
A: terraform import brings an already existing resource into Terraform state. Creating from scratch provisions a new resource using Terraform.
Q2. When would you use state mv?
A: When renaming a resource in configuration without destroying and recreating it.
Q3. When would you use state rm?
A: To remove a resource from Terraform state while keeping it alive in AWS.
Q4. What is State Drift?
A: When actual infrastructure differs from Terraform configuration due to manual changes outside of Terraform.
Q5. How do you fix a stale lock?
A: Use terraform force-unlock <LOCK_ID>

6. When to Use These Commands

terraform state mv → Rename or move resources safely
terraform state rm → Remove resource from state (without destroying)
terraform import → Adopt existing AWS resources
terraform force-unlock → Release stuck locks
terraform refresh → Update state with current real-world state
