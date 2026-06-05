# #90DaysOfDevOps - Day 68

# Introduction to Ansible

## Objective

Learn the fundamentals of Ansible, set up a lab environment, configure inventory files, run ad-hoc commands, and understand how Ansible manages infrastructure through an agentless architecture.

---

# What is Configuration Management?

Configuration Management is the process of managing and maintaining systems in a desired and consistent state.

### Why Do We Need It?

* Automates repetitive administrative tasks.
* Ensures consistency across servers.
* Reduces manual effort and human errors.
* Makes infrastructure scalable and repeatable.
* Simplifies software deployment and updates.

Example:

Instead of logging into 100 servers and installing Git manually, Ansible can perform the task on all servers simultaneously.

---

# How is Ansible Different from Chef, Puppet, and Salt?

| Tool      | Agent Required | Communication |
| --------- | -------------- | ------------- |
| Ansible   | No             | Push-Based    |
| Puppet    | Yes            | Pull-Based    |
| Chef      | Yes            | Pull-Based    |
| SaltStack | Usually Yes    | Push/Pull     |

### Why Ansible?

* Agentless architecture
* Uses SSH
* Easy YAML syntax
* Quick setup
* Less maintenance

---

# What Does Agentless Mean?

Agentless means no software agent needs to be installed on target servers.

Ansible connects directly to managed nodes using SSH and executes tasks remotely.

Benefits:

* Easy management
* Reduced resource usage
* Simplified security
* No agent upgrades required

---

# Ansible Architecture

## Control Node

The machine where Ansible is installed and executed.

In my lab:

* Ubuntu EC2 Instance
* Ansible installed here

## Managed Nodes

Target servers managed by Ansible.

In my lab:

* Ubuntu EC2 Instance #1
* Ubuntu EC2 Instance #2

## Inventory

Contains the list of hosts managed by Ansible.

## Modules

Reusable units of work.

Examples:

* ping
* copy
* apt
* yum
* command
* service

## Playbooks

YAML files used to automate tasks.

---

# Lab Setup

## Environment

I used Terraform-created Ubuntu EC2 instances for my Ansible practice lab.

### Infrastructure

| Component          | Details      |
| ------------------ | ------------ |
| Control Node       | Ubuntu EC2   |
| Managed Node 1     | Ubuntu EC2   |
| Managed Node 2     | Ubuntu EC2   |
| Authentication     | SSH Key Pair |
| Configuration Tool | Ansible      |

---

# Installing Ansible

## Installation

```bash
sudo apt update
sudo apt install ansible -y
```

## Verify Installation

```bash
ansible --version
```

### Why Install Only on the Control Node?

Ansible uses an agentless architecture.

Only the Control Node requires Ansible installation because it communicates with Managed Nodes over SSH.

---

# Inventory Configuration

## inventory.ini

(IPs redacted for public sharing)

```ini
[servers]
SERVER_1 ansible_user=ubuntu ansible_ssh_private_key_file=terra-automate-key
SERVER_2 ansible_user=ubuntu ansible_ssh_private_key_file=terra-automate-key
```

---

# Ansible Configuration

## ansible.cfg

```ini
[defaults]
interpreter_python = /usr/bin/python3.14
host_key_checking = False
inventory = inventory.ini
```

---

# Connectivity Test

## Command

```bash
ansible servers -m ping
```

## Output

```text
SERVER_1 | SUCCESS => {
    "ping": "pong"
}

SERVER_2 | SUCCESS => {
    "ping": "pong"
}
```

### Screenshot

Add Screenshot: <img width="890" height="227" alt="image" src="https://github.com/user-attachments/assets/e7231015-3197-4a27-aeb6-6f1ea7056c0e" />


* ansible servers -m ping

---

# Ad-Hoc Commands

## 1. Check Connectivity

### Command

```bash
ansible servers -m ping
```

### Output

```text
pong
pong
```

---

## 2. Check System Uptime

### Command

```bash
ansible all -i inventory.ini -m command -a "uptime"
```

### Output

```text
up 2 min
load average: 0.04, 0.07, 0.03

up 2 min
load average: 0.55, 0.66, 0.29
```

---

## 3. Check Memory Usage

### Command

```bash
ansible servers -m command -a "free -h"
```

### Output

```text
Mem: 908Mi total
Used: 330Mi
Free: 363Mi

Mem: 908Mi total
Used: 313Mi
Free: 378Mi
```

---

## 4. Check Disk Usage

### Command

```bash
ansible servers -m command -a "df -hT"
```

### Output

```text
Filesystem     Type   Size  Used Avail Use%
/dev/root      ext4   6.7G  2.1G 4.6G  31%
```

---

## 5. Install Git Package

### Command

```bash
ansible servers -i inventory.ini -m apt -a "name=git state=present" --become
```

### Output

```text
SUCCESS
changed: false
```

Git was already installed on both servers.

---

## 6. Copy File to Remote Servers

### Create File

```bash
echo "Hello from Ansible" > hello.txt
```

### Copy File

```bash
ansible all -i inventory.ini -m copy -a "src=hello.txt dest=/tmp/hello.txt"
```

### Output

```text
changed: true
dest: /tmp/hello.txt
```

### Verify

```bash
ansible all -m command -a "cat /tmp/hello.txt"
```

Output:

```text
Hello from Ansible
```

---

# What Does --become Do?

The `--become` option allows Ansible to execute tasks with elevated privileges (sudo).

Example:

```bash
ansible servers -m apt -a "name=git state=present" --become
```

### Common Use Cases

* Installing packages
* Managing services
* Editing system files
* Creating users and groups

---

# Difference Between Command and Shell Modules

| Command Module                  | Shell Module                          |
| ------------------------------- | ------------------------------------- |
| Executes commands directly      | Executes commands through shell       |
| More secure                     | Less secure                           |
| Does not support pipes          | Supports pipes                        |
| Does not support redirects      | Supports redirects                    |
| Recommended for simple commands | Used when shell features are required |

### Command Module Example

```bash
ansible servers -m command -a "uptime"
```

### Shell Module Example

```bash
ansible servers -m shell -a "ps -ef | grep nginx"
```

The shell module is required because pipes (`|`) are shell features.

---

# Key Learnings

* Learned Configuration Management concepts.
* Understood Ansible architecture.
* Installed Ansible on the Control Node.
* Created inventory and configuration files.
* Verified connectivity with managed nodes.
* Executed multiple ad-hoc commands.
* Installed packages remotely.
* Copied files across servers.
* Learned the purpose of `--become`.
* Understood the difference between command and shell modules.

---

# Conclusion

Day 68 focused on learning Ansible fundamentals and setting up a working automation lab. I successfully configured Ansible, connected to managed nodes, executed ad-hoc commands, installed packages, copied files, and explored how Ansible automates server management through an agentless architecture. This forms the foundation for upcoming topics such as Playbooks, Roles, Variables, and Configuration Management automation.
