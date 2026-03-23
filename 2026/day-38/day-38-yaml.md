# Day 38 – YAML Basics

## Objective

The objective of Day 38 was to understand the **basics of YAML**, which is widely used in DevOps tools like **Kubernetes, Docker Compose, GitHub Actions, Ansible, and CI/CD pipelines**.

Today I practiced:

- YAML key-value pairs
- Lists
- Nested objects
- Multi-line strings
- YAML validation

---

# Task 1 – Key Value Pairs

I created a YAML file called **person.yaml** to describe myself.

## person.yaml

```yaml
---
name: Nayan_Marotkar
role: DevOps Engineer
experience_years: 1.5
learning: "true"
tools:
  - YAML
  - Linux
  - Git
  - GitHub
  - shell_script
  - Docker
  - Docker compose
  - CI/CD
hobbies: [ reading, watching movies, gamig ]

---
```

### Command Used

```bash
cat person.yaml
```

### Result

The file displayed correctly and showed:

- Key-value pairs
- YAML lists
- Inline list format

---

# Task 2 – Lists in YAML

I learned that YAML supports **two ways to write lists**.

### 1. Block List Format

```yaml
tools:
  - YAML
  - AWS
  - Kubernetes
  - Terraform
  - GitHub
```

### 2. Inline List Format

```yaml
hobbies: [ reading, watching movies, gamig ]
```

### Key Learning

YAML lists can be written in:

- **Block style** using `-`
- **Inline style** using `[ ]`

---

# Task 3 – Nested Objects

I created another YAML file called **server.yaml** to practice **nested keys**.

## server.yaml

```yaml
server:
  name: nginx
  ip: 0.0.0.0/0
  ports:
    - "8080:8080"
database:
  host: db
  name: my-db
  credential:
    user: root
    password: root

startup_script: |
  #!/bin/bash
  echo "Starting server..."
  # This is a comment within the script
  /usr/bin/my_application --start
   echo "Server started."

# > fold style (folds into one line)
script: >
  #!/bin/bash
  echo "Starting server and performing some maintenance tasks in a single line string."
  # The newlines in the YAML file will be converted to single spaces.
  /usr/bin/my_application --start
```

---

# Task 4 – Multi-line Strings

YAML supports multi-line strings.

### Block Style `|`

Preserves **new lines exactly**.

Example output:

```
#!/bin/bash
echo "Starting server..."
/usr/bin/my_application --start
echo "Server started."
```

### Fold Style `>`

Converts multiple lines into **a single line**.

Example output:

```
#!/bin/bash echo "Starting server and performing some maintenance tasks in a single line string." /usr/bin/my_application --start
```

### When to Use Them

| Style | Use Case |
|------|------|
| `|` | Scripts, configuration blocks |
| `>` | Long paragraphs or messages |

---

# Task 5 – YAML Validation

I validated my YAML files using an online YAML validator.

Validator used:

```
https://www.yamllint.com
```

### Steps Performed

1. Uploaded `person.yaml`
2. Uploaded `server.yaml`
3. Intentionally broke indentation
4. Observed validation errors
5. Fixed indentation
6. Validated the files again

---

# Example Broken YAML

```yaml
name: devops
tools:
- docker
  - kubernetes
```

### Problem

The indentation of the list is incorrect.

### Correct Version

```yaml
name: devops
tools:
  - docker
  - kubernetes
```

---

# Commands Used

```bash
cat person.yaml
cat server.yaml
```

Optional CLI validation:

```bash
yamllint person.yaml
yamllint server.yaml
```

---

# Key Learnings

## 1. YAML Uses Spaces Only

Tabs are **not allowed**.

Incorrect:

```
(tab) name: devops
```

Correct:

```
name: devops
```

---

## 2. Indentation Defines Structure

YAML hierarchy depends on **consistent spacing**.

Example:

```
database
  credentials
    user
    password
```

---

## 3. YAML Supports Multiple Data Structures

YAML can represent:

- Key-value pairs
- Lists
- Nested objects
- Multi-line strings

---

# Verification

### Person File

```bash
cat person.yaml
```

Confirmed:

- Key-value pairs
- Standard list
- Inline list

### Server File

```bash
cat server.yaml
```

Confirmed:

- Nested objects
- Credentials hierarchy
- Multi-line strings

---

# Why YAML is Important in DevOps

YAML is heavily used in modern DevOps tools such as:

- Kubernetes manifests
- Docker Compose
- GitHub Actions
- GitLab CI/CD
- Ansible playbooks
- Terraform configurations

Understanding YAML is essential before writing **CI/CD pipelines and infrastructure configuration files**.

---

# Repository Structure

```
2026/
 └ day-38/
      ├ person.yaml
      ├ server.yaml
      └ day-38-yaml.md
```

---

# Day 38 Status

YAML fundamentals successfully practiced and validated.

---

# Tags

`90DaysOfDevOps`  `DevOps`  `YAML` `TrainWithShubham` `DevOpsLearning`
