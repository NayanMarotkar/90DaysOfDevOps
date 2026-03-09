## Revision Day: Everything from Day 1 to Day 27


## 1. What does chmod 755 script.sh do?

`chmod 755 script.sh` sets permissions for the file.

Permission breakdown:
- Owner: **7 (rwx)** → read, write, execute
- Group: **5 (r-x)** → read, execute
- Others: **5 (r-x)** → read, execute

This means the owner can read, write, and execute the script, while group and others can only read and execute it.

---

## 2. What is the difference between a process and a service?

### Process
A **process** is a running instance of a program.

Characteristics:
- Has a unique **PID (Process ID)**
- Can run in foreground or background
- Created when a program is executed

Example:
```
ps aux
```

### Service
A **service** is a program that runs in the background to provide functionality to the system.

Examples:
- Web server
- Database server
- SSH server

Services are usually managed using **systemd**.

Example:
```
sudo systemctl start nginx
```

Key idea:
A service is usually a **long-running background process managed by the system**.

---

## 3. How do you find which process is using port 8080?

You can run:

```
sudo netstat -tulpn | grep :8080
```

Other modern alternatives:

```
sudo lsof -i :8080
```

or

```
sudo ss -tulpn | grep :8080
```

These commands show the **process name, PID, and port usage**.

---

## 4. What does set -euo pipefail do in a shell script?

It enables **strict error handling** in shell scripts.

```
set -euo pipefail
```

Meaning:
- `-e` → Exit the script if any command fails
- `-u` → Exit if an undefined variable is used
- `-o pipefail` → If any command in a pipeline fails, the pipeline fails

This helps prevent silent errors in scripts.

---

## 5. What is the difference between git reset --hard and git revert?

### git reset --hard
- Moves HEAD to a previous commit
- Deletes changes in staging area and working directory
- Rewrites commit history

Example:
```
git reset --hard HEAD~1
```

Effect:
Last commit and changes are removed.

### git revert
- Creates a new commit that reverses a previous commit
- Does not rewrite history

Example:
```
git revert <commit-id>
```

Effect:
Safely undoes changes without modifying commit history.

---

## 6. What branching strategy would you recommend for a team of 5 developers shipping weekly?

A common strategy is **Feature Branch Workflow**.

Branches:
```
main
develop
feature/*
```

Workflow:
1. `main` contains production-ready code
2. `develop` is used for integration
3. Developers create feature branches for new features

Example:
```
git checkout -b feature/login-system
```

Process:
```
feature → develop → main
```

Benefits:
- Cleaner commit history
- Easier collaboration
- Safer releases

---

## 7. What does git stash do and when would you use it?

`git stash` temporarily saves **uncommitted changes** so you can switch branches without committing them.

Example:

Save changes:
```
git stash
```

View stashes:
```
git stash list
```

Restore changes:
```
git stash pop
```

Use case:
When you are working on something but need to switch branches quickly without committing unfinished work.

---

## 8. How do you schedule a script to run every day at 3 AM?

Use **cron jobs**.

Open the cron editor:

```
crontab -e
```

Add this line:

```
0 3 * * * /path/to/script.sh
```

Cron format:

```
minute hour day month day_of_week
```

`0 3 * * *` means **run every day at 3:00 AM**.

---

## 9. What is the difference between git fetch and git pull?

### git fetch
Downloads changes from the remote repository but **does not merge them** into your local branch.

Example:
```
git fetch origin
```

### git pull
Downloads changes and **merges them into your current branch**.

Example:
```
git pull origin main
```

In simple terms:

```
git pull = git fetch + git merge
```

---

## 10. What is LVM and why would you use it instead of regular partitions?

LVM stands for **Logical Volume Manager**.

It provides flexible disk management compared to traditional disk partitions.

Advantages:
- Resize partitions easily
- Extend storage without downtime
- Combine multiple disks into a single logical volume
- Create snapshots for backups

Structure:

```
Physical Disk
   ↓
Physical Volume (PV)
   ↓
Volume Group (VG)
   ↓
Logical Volume (LV)
```

Logical volumes behave like normal partitions but are easier to resize and manage.
