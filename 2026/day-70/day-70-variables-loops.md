# Day 70 - Ansible Variables, Facts, Conditionals, Loops, and Register

## Objective

Learn how to use:

- Variables (`group_vars` and `host_vars`)
- Ansible Facts
- Conditional Statements (`when`)
- Loops (`loop`)
- Register Variables
- Dynamic Server Reporting

---

# Task 1: Working with Variables

## Project Structure

```text
Ansible-Practice/
├── ansible.cfg
├── hosts
├── group_vars/
│   └── all.yml
├── host_vars/
│   ├── 18.217.27.134.yml
│   └── 18.219.55.132.yml
├── playbook/
│   ├── variables-demo.yml
│   ├── conditional-demo.yml
│   ├── loop.yml
│   └── server-reports.yml
└── screenshots/
```

---

## group_vars/all.yml

```yaml
app_env: deployment

web_packages:
  - nginx

max_connections: 2000
```

---

## host_vars/18.217.27.134.yml

```yaml
server_role: web
max_connections: 5000
```

---

## host_vars/18.219.55.132.yml

```yaml
server_role: database
```

---

# Variable Precedence

Ansible follows a hierarchy when multiple variables have the same name.

Higher precedence values override lower precedence values.

### Example

**group_vars/all.yml**

```yaml
max_connections: 2000
```

**host_vars/18.217.27.134.yml**

```yaml
max_connections: 5000
```

### Result

| Host | Value |
|--------|--------|
| 18.217.27.134 | 5000 |
| 18.219.55.132 | 2000 |

Because `host_vars` has higher precedence than `group_vars`.

---

# Task 2: Working with Ansible Facts

Facts are automatically collected system information.

### Useful Facts

| Fact | Description | Use Case |
|--------|--------|--------|
| ansible_distribution | OS Name | OS-specific package installation |
| ansible_distribution_version | OS Version | Version-based conditions |
| ansible_memtotal_mb | Total RAM | Capacity checks |
| ansible_default_ipv4.address | Primary IP Address | Reporting and monitoring |
| ansible_hostname | Hostname | Inventory and reports |

---

## Example

```yaml
- debug:
    msg: "{{ ansible_distribution }}"
```

Output:

```text
Ubuntu
```

---

# Task 3: Conditional Playbook

## conditional-demo.yml

Used the `when` keyword to execute tasks only when conditions are met.

### Conditions Tested

- Install packages only on Ubuntu
- Display warning when RAM < 1GB
- Environment-specific execution
- Multiple AND conditions
- OR conditions

---

## Example

```yaml
- name: Run only on Ubuntu
  debug:
    msg: "This is an Ubuntu machine"
  when: ansible_distribution == "Ubuntu"
```

---

## Result

### Executed Tasks

```text
TASK [Run only on Ubuntu]
ok: [18.217.27.134]
ok: [18.219.55.132]
```

### Skipped Tasks

```text
TASK [Multiple conditions (AND)]
skipping: [18.217.27.134]
skipping: [18.219.55.132]
```

📸 Screenshot:
`conditional-playbook-output.png`

---

# Task 4: Loops

## loop.yml

Created multiple users, directories, and packages using loops.

---

## Create Users

```yaml
- name: Create multiple users
  user:
    name: "{{ item.name }}"
    groups: "{{ item.groups }}"
    state: present
  loop: "{{ users }}"
```

---

## Create Directories

```yaml
- name: Create multiple directories
  file:
    path: "{{ item }}"
    state: directory
    mode: '0755'
  loop: "{{ directories }}"
```

---

## Install Packages

```yaml
- name: Install multiple packages
  apt:
    name: "{{ item }}"
    state: present
  loop:
    - git
    - curl
    - unzip
    - jq
```

---

## Loop Output

```text
changed: [18.217.27.134] => (item={'name': 'deploy', 'groups': 'wheel'})
changed: [18.217.27.134] => (item={'name': 'monitor', 'groups': 'wheel'})
changed: [18.217.27.134] => (item={'name': 'appuser', 'groups': 'users'})
```

Each loop iteration is executed independently.

📸 Screenshot:
`loop-playbook-output.png`

---

# Difference Between loop and with_items

## Old Syntax

```yaml
with_items:
  - git
  - curl
```

---

## Modern Syntax

```yaml
loop:
  - git
  - curl
```

---

## Why loop is Preferred

| loop | with_items |
|--------|--------|
| Modern syntax | Legacy syntax |
| More readable | Older style |
| Supports advanced looping | Limited |
| Recommended by Ansible | Deprecated approach |

**Recommendation:** Always use `loop`.

---

# Verification of Loop Tasks

## Users Created

```bash
ansible all -m command -a "id deploy"
ansible all -m command -a "id monitor"
ansible all -m command -a "id appuser"
```

### Output

```text
uid=1001(deploy) gid=1002(deploy)
uid=1002(monitor) gid=1003(monitor)
uid=1003(appuser) gid=1004(appuser)
```

---

## Directories Created

```bash
ansible all -m shell -a "ls -ld /opt/app/*"
```

### Output

```text
/opt/app/config
/opt/app/data
/opt/app/logs
/opt/app/tmp
```

---

## Packages Installed

```bash
ansible all -m command -a "which git"
ansible all -m command -a "which jq"
```

### Output

```text
/usr/bin/git
/usr/bin/jq
```

---

# Task 5: Register Variables

Register variables store command output for later use.

Example:

```yaml
- name: Check disk space
  command: df -h /
  register: disk_result
```

The output can later be referenced as:

```yaml
{{ disk_result.stdout }}
```

---

# Task 6: Server Health Report

## server-reports.yml

Collected:

- Disk Usage
- Memory Usage
- Running Services
- Host Information

Generated a report file on every server.

---

## Registered Variables

```yaml
disk_result
memory_result
services_result
```

---

## Generated Report

```text
==================================
Server Report
==================================

Server: 18.217.27.134
OS: Ubuntu 26.04
IP Address: 172.31.38.165
Total RAM: 908 MB

----- Disk Usage -----
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       6.7G  2.3G  4.4G  34% /

----- Memory Usage -----
Mem: 908 338 222 2 462 570

----- Running Services -----
acpid.service
chrony.service
cron.service
dbus.service
ssh.service

Checked At: 2026-06-06T13:09:44Z
```

---

## Verify Report File

```bash
ansible all -m shell -a "cat /tmp/server-report-*"
```

### Result

Reports were successfully generated on both servers.

```text
/tmp/server-report-18.217.27.134.txt
/tmp/server-report-18.219.55.132.txt
```

---

# Key Learnings

- Used `group_vars` and `host_vars` for centralized configuration.
- Learned variable precedence and overriding values.
- Gathered and used Ansible Facts.
- Applied conditional execution using `when`.
- Automated repetitive tasks using `loop`.
- Used `register` to capture command output.
- Built a real-world server health reporting playbook.
- Generated and verified reports on multiple servers.

---

# Commands Used

```bash
ansible-playbook playbook/conditional-demo.yml

ansible-playbook playbook/loop.yml

ansible-playbook playbook/server-reports.yml

ansible all -m command -a "id deploy"

ansible all -m shell -a "ls -ld /opt/app/*"

ansible all -m shell -a "cat /tmp/server-report-*"
```

---

## Day 70 Summary

Day 70 focused on making playbooks dynamic and intelligent using variables, facts, conditions, loops, and registered outputs. By the end of the day, I was able to create reusable automation, perform system health checks, and generate detailed server reports across multiple Ubuntu servers using Ansible.
