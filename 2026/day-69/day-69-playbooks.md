# #90DaysOfDevOps - Day 69

# Ansible Playbooks and Modules

## Objective

Learn how to create and execute Ansible Playbooks, understand Plays, Tasks, Modules, and Handlers, and automate server configuration using reusable YAML files.

---

# Introduction

Ad-hoc commands are useful for quick administrative tasks, but real infrastructure automation is achieved through Playbooks.

A Playbook is a YAML file that describes the desired state of systems. Once written, it can be executed repeatedly to ensure servers remain configured consistently.

Benefits of Playbooks:

* Infrastructure as Code (IaC)
* Repeatable deployments
* Consistent server configurations
* Easy automation and maintenance
* Idempotent execution

---

# Task 1: My First Playbook

## install-nginx.yml

```yaml
---
- name: Install and Start Nginx
  hosts: servers
  become: true

  tasks:

    - name: Install Nginx
      apt:
        name: nginx
        state: present

    - name: Start and Enable Nginx
      service:
        name: nginx
        state: started
        enabled: true

    - name: Create Custom Index Page
      copy:
        content: "<h1>Deployed by Ansible - TerraWeek Server</h1>"
        dest: /var/www/html/index.html
```

## Run Playbook

```bash
ansible-playbook install-nginx.yml
```

### First Run

```text
TASK [Install Nginx] ***************
changed

TASK [Start and Enable Nginx] ******
changed

TASK [Create Custom Index Page] ****
changed
```

### Second Run (Idempotency)

```text
TASK [Install Nginx] ***************
ok

TASK [Start and Enable Nginx] ******
ok

TASK [Create Custom Index Page] ****
ok
```

### What is Idempotency?

Idempotency means running the same playbook multiple times produces the same result without making unnecessary changes.

---

# Task 2: Understanding Playbook Structure

## Example Structure

```yaml
---
- name: Play Name
  hosts: servers
  become: true

  tasks:

    - name: Task Name
      module_name:
        key: value
```

## Components

### Play

A Play maps a group of hosts to tasks.

Example:

```yaml
- name: Configure Web Servers
  hosts: web
```

### Task

A Task is a single unit of work.

Example:

```yaml
- name: Install Nginx
  apt:
    name: nginx
    state: present
```

### Module

Modules perform actual operations.

Examples:

* apt
* copy
* file
* service
* command
* shell

---

## Interview Questions

### Difference Between Play and Task

| Play                   | Task            |
| ---------------------- | --------------- |
| Targets hosts          | Performs work   |
| Contains tasks         | Single action   |
| Can contain many tasks | Uses one module |

---

### Can We Have Multiple Plays In One Playbook?

Yes.

A single playbook can contain multiple plays targeting different host groups.

---

### become: true At Play Level vs Task Level

Play Level:

```yaml
become: true
```

Applies to every task.

Task Level:

```yaml
- name: Install Package
  become: true
```

Applies only to that task.

---

### What Happens If A Task Fails?

By default:

* Play stops on that host.
* Remaining tasks for that host are skipped.
* Other hosts continue execution.

---

# Task 3: Essential Ansible Modules

## Package Installation

### apt Module

```yaml
- name: Install Packages
  apt:
    name:
      - git
      - curl
      - wget
      - tree
    state: present
```

Purpose:

Installs software packages.

---

## Service Module

```yaml
- name: Ensure Nginx Running
  service:
    name: nginx
    state: started
    enabled: true
```

Purpose:

Manage services.

---

## Copy Module

```yaml
- name: Copy Config File
  copy:
    src: files/app.conf
    dest: /etc/app.conf
    owner: root
    group: root
    mode: '0644'
```

Purpose:

Copies files from Control Node to Managed Nodes.

---

## File Module

```yaml
- name: Create Application Directory
  file:
    path: /opt/myapp
    state: directory
    owner: ubuntu
    mode: '0755'
```

Purpose:

Create files, directories, and manage permissions.

---

## Command Module

```yaml
- name: Check Disk Space
  command: df -h
  register: disk_output

- name: Display Output
  debug:
    var: disk_output.stdout_lines
```

Purpose:

Execute commands without shell features.

---

## Shell Module

```yaml
- name: Count Running Processes
  shell: ps aux | wc -l
  register: process_count

- name: Display Count
  debug:
    msg: "Total Processes: {{ process_count.stdout }}"
```

Purpose:

Execute commands using shell features.

---

## lineinfile Module

```yaml
- name: Set Timezone
  lineinfile:
    path: /etc/environment
    line: 'TZ=Asia/Kolkata'
    create: true
```

Purpose:

Add or modify a specific line in a file.

---

# Difference Between Command and Shell Modules

| Command Module           | Shell Module         |
| ------------------------ | -------------------- |
| Direct command execution | Uses system shell    |
| More secure              | Less secure          |
| No pipes supported       | Pipes supported      |
| No redirects supported   | Redirects supported  |
| Recommended by default   | Use only when needed |

### Command Example

```yaml
command: df -h
```

### Shell Example

```yaml
shell: ps aux | wc -l
```

---

# Task 4: Handlers

Handlers execute only when notified by a task.

## nginx-config.yml

```yaml
---
- name: Configure Nginx
  hosts: servers
  become: true

  tasks:

    - name: Install Nginx
      apt:
        name: nginx
        state: present

    - name: Deploy Nginx Config
      copy:
        src: files/nginx.conf
        dest: /etc/nginx/nginx.conf
      notify: Restart Nginx

    - name: Deploy Index Page
      copy:
        content: "<h1>Managed by Ansible</h1>"
        dest: /var/www/html/index.html

  handlers:

    - name: Restart Nginx
      service:
        name: nginx
        state: restarted
```

---

## Handler Workflow

### First Run

```text
Copy Config -> changed
Notify Handler -> triggered
Restart Nginx -> executed
```

### Second Run

```text
Copy Config -> ok
Notify Handler -> not triggered
Restart Nginx -> skipped
```

### Benefits

* Prevent unnecessary service restarts
* Faster execution
* Better production practices

---

# Task 5: Check Mode, Diff Mode, and Verbosity

## Check Mode

Preview changes without making modifications.

```bash
ansible-playbook install-nginx.yml --check
```

---

## Diff Mode

Show actual file differences.

```bash
ansible-playbook nginx-config.yml --check --diff
```

---

## Verbose Output

```bash
ansible-playbook install-nginx.yml -v
```

More detail:

```bash
ansible-playbook install-nginx.yml -vv
```

Connection debugging:

```bash
ansible-playbook install-nginx.yml -vvv
```

---

## List Hosts

```bash
ansible-playbook install-nginx.yml --list-hosts
```

---

## List Tasks

```bash
ansible-playbook install-nginx.yml --list-tasks
```

---

## Why Is --check --diff Important?

Benefits:

* Preview changes before deployment
* Detect mistakes safely
* Reduce production risks
* Validate configuration changes
* Review exact file modifications

This is one of the safest ways to test infrastructure changes before applying them.

---

# Task 6: Multiple Plays In One Playbook

## multi-play.yml

```yaml
---
- name: Configure Web Servers
  hosts: web
  become: true

  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present

- name: Configure App Servers
  hosts: app
  become: true

  tasks:
    - name: Install Build Tools
      apt:
        name:
          - gcc
          - make
        state: present

- name: Configure Database Servers
  hosts: db
  become: true

  tasks:
    - name: Install MySQL Client
      apt:
        name: mysql-client
        state: present
```

## Run Playbook

```bash
ansible-playbook multi-play.yml
```

### Verification

* Nginx installed only on Web Servers
* Build tools installed only on App Servers
* MySQL Client installed only on Database Servers

---

# Screenshots To Include

## Screenshot 1 - <img width="1548" height="674" alt="image" src="https://github.com/user-attachments/assets/8ce98722-e800-4064-8287-390b48420218" />
<img width="1532" height="745" alt="image" src="https://github.com/user-attachments/assets/5af71f68-2317-4a43-b43c-d9f7b124526a" />
<img width="1523" height="655" alt="image" src="https://github.com/user-attachments/assets/3b4346e2-fa7b-42c0-9c64-34601cbfbd07" />

---

# Key Learnings

* Learned Ansible Playbook structure.
* Understood Plays, Tasks, Modules, and Handlers.
* Created reusable infrastructure automation.
* Learned idempotent execution.
* Used essential modules:

  * apt
  * service
  * copy
  * file
  * command
  * shell
  * lineinfile
* Implemented handlers for efficient service management.
* Learned production-safe execution using:

  * --check
  * --diff
  * -v
* Created multi-play playbooks.

---

# Conclusion

Day 69 focused on Ansible Playbooks and Modules. I learned how to automate server configuration using YAML-based playbooks, manage services and files through modules, implement handlers for conditional actions, and safely preview infrastructure changes using check and diff modes. These concepts form the foundation for real-world Infrastructure as Code and configuration management practices.
