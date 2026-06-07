# Day 72 – Ansible Project: Automate Docker and Nginx Deployment

## Objective

The goal of Day 72 was to combine all major Ansible concepts learned during the previous days into a complete infrastructure automation project.

Using Ansible Roles, Templates, Variables, Handlers, Tags, Vault, and Playbooks, I automated the deployment of:

* Docker Engine
* Docker Container
* Nginx Reverse Proxy
* Docker Hub Authentication (Vault Ready)
* End-to-End Application Deployment

The entire environment can now be deployed with a single Ansible command.

---

# Project Architecture

```text
                +----------------+
                |  Ansible Node  |
                +--------+-------+
                         |
                         |
                 SSH Automation
                         |
                         v
        +----------------------------------+
        |          Managed Server          |
        |                                  |
        |    Nginx Reverse Proxy :80       |
        |              |                   |
        |              v                   |
        |     Docker Container :8080       |
        |                                  |
        +----------------------------------+
```

Request Flow:

```text
User Browser
      |
      v
Server IP :80
      |
      v
Nginx Reverse Proxy
      |
      v
Docker Container :8080
```

---

# Project Directory Structure

```text
ansible-docker-project/
│
├── ansible.cfg
├── inventory.ini
├── site.yml
│
├── group_vars/
│   └── all.yml
│
├── roles/
│   ├── common/
│   │   └── tasks/
│   │       └── main.yml
│   │
│   ├── docker/
│   │   ├── defaults/
│   │   │   └── main.yml
│   │   ├── handlers/
│   │   │   └── main.yml
│   │   └── tasks/
│   │       └── main.yml
│   │
│   └── nginx/
│       ├── handlers/
│       │   └── main.yml
│       ├── tasks/
│       │   └── main.yml
│       └── templates/
│           └── app-proxy.conf.j2
│
└── day-72-ansible-project.md
```

---

# Inventory Configuration

```ini
[web]
52.14.31.155
18.220.83.24

[web:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/ansible-key.pem
```

---

# Ansible Configuration

```ini
[defaults]
inventory = inventory.ini
host_key_checking = False
```

---

# Common Variables

File:

```text
group_vars/all.yml
```

```yaml
---
timezone: Asia/Kolkata

project_name: devops-app

app_env: development

common_packages:
  - vim
  - curl
  - wget
  - git
  - htop
  - tree
  - jq
  - unzip
```

---

# Master Playbook

File:

```text
site.yml
```

```yaml
---
- name: Common setup
  hosts: all
  become: true

  roles:
    - common

- name: Docker setup
  hosts: web
  become: true

  roles:
    - docker

- name: Nginx setup
  hosts: web
  become: true

  roles:
    - nginx
```

---

# Common Role

File:

```text
roles/common/tasks/main.yml
```

Responsibilities:

* Update package cache
* Install utility packages
* Configure hostname
* Configure timezone
* Create deploy user

---

# Docker Role

File:

```text
roles/docker/tasks/main.yml
```

Responsibilities:

* Install Docker dependencies
* Add Docker repository
* Install Docker CE
* Start Docker service
* Install Docker Compose
* Add deploy user to Docker group
* Pull application image
* Run Docker container
* Verify container health

Container Configuration:

```yaml
docker_app_image: nginx
docker_app_tag: latest
docker_app_name: myapp

docker_app_port: 8080
docker_container_port: 80
```

Container Deployment:

```yaml
community.docker.docker_container:
  name: myapp
  image: nginx:latest
  state: started
  restart_policy: always

  ports:
    - "8080:80"
```

---

# Nginx Role

File:

```text
roles/nginx/tasks/main.yml
```

Responsibilities:

* Install Nginx
* Remove default site
* Deploy reverse proxy configuration
* Validate Nginx configuration
* Enable and start Nginx

---

# Nginx Reverse Proxy Template

File:

```text
roles/nginx/templates/app-proxy.conf.j2
```

```nginx
upstream docker_app {
    server 127.0.0.1:8080;
}

server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://docker_app;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /health {
        return 200 'OK';
    }

    error_log /var/log/nginx/devops-app_debug.log debug;
}
```

---

# Ansible Tags Used

Selective deployment was performed using tags.

Run only Docker tasks:

```bash
ansible-playbook site.yml --tags docker
```

Run only Nginx tasks:

```bash
ansible-playbook site.yml --tags nginx
```

Skip common setup:

```bash
ansible-playbook site.yml --skip-tags common
```

Benefits:

* Faster deployments
* Easier troubleshooting
* Role-specific updates

---

# Ansible Vault

Docker Hub credentials were protected using Ansible Vault.

Vault file:

```text
group_vars/web/vault.yml
```

Example:

```yaml
vault_docker_username: username
vault_docker_password: token
```

Encryption:

```bash
ansible-vault create group_vars/web/vault.yml
```

Benefits:

* Secrets are encrypted at rest
* Passwords are not stored in plain text
* Safe for version control repositories

---

# Deployment Execution

Dry Run:

```bash
ansible-playbook site.yml --check --diff
```

Production Deployment:

```bash
ansible-playbook site.yml
```

Result:

```text
PLAY RECAP

18.220.83.24 : ok=25 changed=4 failed=0
52.14.31.155 : ok=25 changed=4 failed=0
```

---

# Verification

## Verify Running Container

Command:

```bash
ansible all -b -m shell -a "docker ps"
```

Expected Output:

```text
CONTAINER ID   IMAGE          STATUS
83afec7635cc   nginx:latest   Up
fbfe87f9e392   nginx:latest   Up
```

📸 Screenshot:
Insert screenshot of docker ps output here.

---

## Verify Nginx Reverse Proxy

Command:

```bash
curl http://52.14.31.155
```

Output:

```html
Welcome to nginx!
```

📸 Screenshot:
Insert screenshot showing curl output here.

---

# Idempotency Test

The playbook was executed a second time.

Command:

```bash
ansible-playbook site.yml
```

Expected:

```text
changed=0
failed=0
```

This demonstrates that the infrastructure is idempotent and Ansible only applies changes when required.

📸 Screenshot:
Insert screenshot of second successful run here.

---

# Screenshots Required

1. Full playbook execution (`ansible-playbook site.yml`)
2. Second run proving idempotency
3. Docker container running (`docker ps`)
4. Curl request to port 80 through Nginx
5. Optional: Nginx configuration validation (`nginx -t`)

---

# Key Concepts Used

| Day | Concept                                |
| --- | -------------------------------------- |
| 68  | Inventory, Ad-hoc Commands, SSH        |
| 69  | Playbooks, Modules, Handlers           |
| 70  | Variables, Facts, Loops, Conditionals  |
| 71  | Roles, Templates, Galaxy, Vault        |
| 72  | Complete End-to-End Automation Project |

---

# Learning Outcome

Day 72 brought together all major Ansible concepts into a real-world deployment project.

Achievements:

* Built reusable Ansible roles
* Automated Docker installation
* Automated container deployment
* Configured Nginx reverse proxy
* Used templates for dynamic configuration
* Protected secrets with Vault
* Performed idempotent deployments
* Managed infrastructure using a single playbook

This project represents a production-style Ansible deployment workflow and demonstrates how infrastructure can be managed consistently, repeatedly, and automatically.
