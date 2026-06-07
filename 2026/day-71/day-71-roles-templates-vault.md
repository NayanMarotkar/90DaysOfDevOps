
# Day 71 — Ansible Roles, Jinja2 Templates, Galaxy & Vault

## Overview

Today’s focus was on structuring real-world automation using:

- :contentReference[oaicite:0]{index=0} Roles (modular automation structure)
- :contentReference[oaicite:1]{index=1} (dynamic configuration generation)
- :contentReference[oaicite:2]{index=2} (pre-built reusable roles)
- :contentReference[oaicite:3]{index=3} (secure secret storage)

This day helped transition from simple playbooks → production-grade automation design.

---

# Task 1 — Jinja2 Templates

## Template File: `templates/nginx-vhost.conf.j2`

```nginx
# Managed by Ansible -- do not edit manually

server {
    listen {{ http_port | default(80) }};
    server_name {{ ansible_hostname }};

    root /var/www/{{ app_name }};
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    access_log /var/log/nginx/{{ app_name }}_access.log;
    error_log /var/log/nginx/{{ app_name }}_error.log;
}
````

---

## Playbook: `template-demo.yml`

```yaml
- name: Deploy Nginx with template
  hosts: web
  become: true

  vars:
    app_name: terraweek-app
    http_port: 80

  tasks:
    - name: Install Nginx
      yum:
        name: nginx
        state: present

    - name: Create web root
      file:
        path: "/var/www/{{ app_name }}"
        state: directory
        mode: '0755'

    - name: Deploy vhost config from template
      template:
        src: templates/nginx-vhost.conf.j2
        dest: "/etc/nginx/conf.d/{{ app_name }}.conf"
      notify: Restart Nginx

    - name: Deploy index page
      copy:
        content: "<h1>{{ app_name }}</h1><p>Host: {{ ansible_hostname }} | IP: {{ ansible_default_ipv4.address }}</p>"
        dest: "/var/www/{{ app_name }}/index.html"

  handlers:
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted
```

---

## Verification Output

```bash
ansible-playbook template-demo.yml --diff
```

### Result:

* Variables were successfully replaced
* Nginx config generated dynamically
* Hostname + IP rendered correctly

---

# Task 2 — Understanding Role Structure

Generated using:

```bash
ansible-galaxy init roles/webserver
```

## Role Directory Structure

```
roles/
  webserver/
    tasks/
      main.yml
    handlers/
      main.yml
    templates/
    files/
    vars/
    defaults/
    meta/
```

---

## Key Difference

| File              | Purpose                                               |
| ----------------- | ----------------------------------------------------- |
| defaults/main.yml | Low priority variables (can be overridden)            |
| vars/main.yml     | High priority variables (cannot be easily overridden) |

---

# Task 3 — Custom Webserver Role

## defaults/main.yml

```yaml
http_port: 80
app_name: myapp
max_connections: 512
```

---

## tasks/main.yml

```yaml
- name: Install Nginx
  yum:
    name: nginx
    state: present

- name: Deploy vhost config
  template:
    src: vhost.conf.j2
    dest: /etc/nginx/conf.d/{{ app_name }}.conf
  notify: Restart Nginx

- name: Create web root
  file:
    path: "/var/www/{{ app_name }}"
    state: directory
    mode: '0755'

- name: Deploy index page
  template:
    src: index.html.j2
    dest: "/var/www/{{ app_name }}/index.html"

- name: Start Nginx
  service:
    name: nginx
    state: started
    enabled: true
```

---

## handlers/main.yml

```yaml
- name: Restart Nginx
  service:
    name: nginx
    state: restarted
```

---

## templates/index.html.j2

```html
<h1>{{ app_name }}</h1>
<p>Server: {{ ansible_hostname }}</p>
<p>IP: {{ ansible_default_ipv4.address }}</p>
<p>Environment: {{ app_env | default('development') }}</p>
<p>Managed by Ansible</p>
```

---

## site.yml (Role Execution)

```yaml
- name: Configure web servers
  hosts: web
  become: true
  roles:
    - role: webserver
      vars:
        app_name: terraweek
        http_port: 80
```

---

## Verification

```bash
ansible-playbook site.yml
curl http://<server-ip>
```

✔ Custom dynamic page loaded successfully

---

# Task 4 — Ansible Galaxy Roles

## Install Role

```bash
ansible-galaxy install geerlingguy.docker
```

## List Installed Roles

```bash
ansible-galaxy list
```

---

## docker-setup.yml

```yaml
- name: Install Docker using Galaxy role
  hosts: app
  become: true
  roles:
    - geerlingguy.docker
```

---

## requirements.yml

```yaml
roles:
  - name: geerlingguy.docker
    version: "7.4.1"
  - name: geerlingguy.ntp
```

---

## Install All Roles

```bash
ansible-galaxy install -r requirements.yml
```

---

## Why use requirements.yml?

* Centralized dependency management
* Version control for roles
* CI/CD friendly automation
* Reproducible environments across teams

---

# Task 5 — Ansible Vault (Secrets Management)

## Create Encrypted File

```bash
ansible-vault create group_vars/db/vault.yml
```

## Example Content

```yaml
vault_db_password: SuperSecretP@ssw0rd
vault_db_root_password: R00tP@ssw0rd123
vault_api_key: sk-abc123xyz789
```

---

## Vault Operations

```bash
ansible-vault view group_vars/db/vault.yml
ansible-vault edit group_vars/db/vault.yml
ansible-vault encrypt group_vars/db/secrets.yml
```

---

## Using Vault Password File

```bash
echo "YourVaultPassword" > .vault_pass
chmod 600 .vault_pass
```

Run playbook:

```bash
ansible-playbook db-setup.yml --vault-password-file .vault_pass
```

---

## Why vault-password-file is better?

* Works in CI/CD pipelines (no manual input)
* Enables automation workflows
* Avoids blocking interactive prompts
* More secure for production deployments

---

# Task 6 — Combined Site Deployment

## site.yml

```yaml
- name: Configure web servers
  hosts: web
  become: true
  roles:
    - webserver

- name: Configure app servers
  hosts: app
  become: true
  roles:
    - geerlingguy.docker

- name: Configure DB servers
  hosts: db
  become: true

  tasks:
    - name: Create DB config with secrets
      template:
        src: templates/db-config.j2
        dest: /etc/db-config.env
        mode: '0600'
```

---

## db-config.j2

```env
DB_HOST={{ ansible_default_ipv4.address }}
DB_PORT={{ db_port | default(3306) }}
DB_PASSWORD={{ vault_db_password }}
DB_ROOT_PASSWORD={{ vault_db_root_password }}
```

---

## Verification

```bash
ansible-playbook site.yml
```

### Check on DB server:

```bash
cat /etc/db-config.env
ls -l /etc/db-config.env
```

✔ Secrets rendered correctly
✔ File permission enforced as 600

---

# Key Learnings

## Roles vs Playbooks vs Ad-hoc

| Type            | Use Case                                |
| --------------- | --------------------------------------- |
| Ad-hoc commands | Quick one-time tasks                    |
| Playbooks       | Step-by-step automation                 |
| Roles           | Reusable, production-grade architecture |

---

# Final Outcome

✔ Custom Ansible role created
✔ Jinja2 dynamic configuration working
✔ Galaxy role installed and used
✔ Vault secrets securely managed
✔ Full multi-server automation deployed

---

# Reflection

This day moved automation from:
**scripts → structured infrastructure automation**

Roles + Templates + Vault = Production-ready DevOps workflow.

```

---

If you want, I can also:
- :contentReference[oaicite:4]{index=4}
- Or :contentReference[oaicite:5]{index=5}
- Or :contentReference[oaicite:6]{index=6}
```
