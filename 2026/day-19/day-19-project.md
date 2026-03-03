Day 19 – Shell Scripting Project: Log Rotation, Backup & Crontab


Task 1: Log Rotation Script
Create log_rotate.sh that:

Takes a log directory as an argument (e.g., /var/log/myapp)
Compresses .log files older than 7 days using gzip
Deletes .gz files older than 30 days
Prints how many files were compressed and deleted
Exits with an error if the directory doesn't exist


Scripts - 
-----------------------
#!/bin/bash
set -euo pipefail

log_rotate() {

    if [ $# -eq 0 ]; then
        echo "Usage: $0 <path to log dir>"
        return 1
    fi

    local Log_dir="$1"

    if [ ! -d "$Log_dir" ]; then
        echo "Log Directory does not exist: $Log_dir"
        return 1
    fi

    compressed=$(find "$Log_dir" -type f -name "*.txt" -mtime +7 -print -exec gzip {} \; | wc -l)

    deleted=$(find "$Log_dir" -type f -name "*.gz" -mtime +30 -print -delete | wc -l)

    echo "Compressed files: $compressed"
    echo "Deleted files: $deleted"
}

log_rotate "/home/ubuntu/scripts/app-data"
------------------------------------

Task 2: Server Backup Script
Create backup.sh that:

Takes a source directory and backup destination as arguments
Creates a timestamped .tar.gz archive (e.g., backup-2026-02-08.tar.gz)
Verifies the archive was created successfully
Prints archive name and size
Deletes backups older than 14 days from the destination
Handles errors — exit if source doesn't exist

Scripts - 
------------------------------
#! /bin/bash

set -euo pipefail

backup() {
        if [ $# -ne 2 ]; then 
                echo "Usage: $0 <source> <backup>"
                return 1

        fi

        local src="$1"
        local dest="$2"

        if [ ! -d "$src" ]; then
                echo "error: source dir does not exist = $src"
                return 1
        fi

        mkdir -p "$dest"

        local data=$(date '+%Y-%m-%d-%H-%m-%S')

        file="$dest/backup-$(date).tar.gz"

        tar -cvzf "$file" "$src" >/dev/null

        if [ -f "$file" ]; then
                echo "backup is created = $file"
                echo "size: $(du -sh "$file" | cut -f1)"
        else
                echo "Backup failed."
                  return 1
        fi

          find "$dest" -name "backup-*.tar.gz" -mtime +14 -delete

}


backup "/home/ubuntu/scripts/app-data" "/home/ubuntu/scripts/backup"
------------------------------------

Task 3: Crontab
Read: crontab -l — what's currently scheduled?
Understand cron syntax:
* * * * *  command
│ │ │ │ │
│ │ │ │ └── Day of week (0-7)
│ │ │ └──── Month (1-12)
│ │ └────── Day of month (1-31)
│ └──────── Hour (0-23)
└────────── Minute (0-59)
Cron entries for:
Run log_rotate.sh every day at 2 AM : 0 2 * * *
Run backup.sh every Sunday at 3 AM : 0 3 * * 7
Run a health check script every 5 minutes : */5 * * * *

---------------------------------------

Task 4: Combine — Scheduled Maintenance Script
Create maintenance.sh that:

Calls your log rotation function
Calls your backup function
Logs all output to /var/log/maintenance.log with timestamps
Write the cron entry to run it daily at 1 AM

scripts -
----------------------------------
#!/bin/bash
set -euo pipefail

LOG_FILE="/home/ubuntu/scripts/maintenance.log"

# Source the scripts with functions
source "/home/ubuntu/scripts/log_rotate.sh"
source "/home/ubuntu/scripts/log_backups.sh"


# Log timestamp and run maintenance
{
    echo "===== $(date) ====="
    log_rotate "/var/log/myapp"
    backup "/home/ubuntu/scripts/app-data" "/home/ubuntu/backups"
} >> "$LOG_FILE" 2>&1

--------------------------

what i learn -
- log rotation how to write them as a function and reuse when you need
- cron job - I set up cronjob for log rotation where it will run every 7 days.
- it will delete logs older then 30 days
- how to handle error in scripts
- Compression - Used tar to compress large files and take their backup
- calling function from other scripts to use in your scripts
  
