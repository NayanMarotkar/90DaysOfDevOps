Day 18 – Shell Scripting: Functions & intermediate Concepts

Task 1: Basic Functions
Create functions.sh with:
A function greet that takes a name as argument and prints Hello, <name>!
A function add that takes two numbers and prints their sum
Call both functions from the script

script =
------------
#! /bin/bash

# define greet function
greet() {
        name=$1
        echo "Hello, $name!"

}

# define add function
add() {
        num1=$1
        num2=$2
        sum=$(( num1 + num2 ))
        echo "the sum of $num1 and $num2 is = $sum"
}

# calling both function

greet "Nayan"
add 17 22
--------------------

Task 2: Functions with Return Values
Create disk_check.sh with:
A function check_disk that checks disk usage of / using df -h
A function check_memory that checks free memory using free -h
A main section that calls both and prints the results

script -
------------------------
#! /bin/bash

# function to check disk usage of / dir
disk_check() {
        echo "-------------------Disk Usage Details----------------------- "
        df -h / | awk 'NR==2{print " Filesystem: " $1, " Size: " $2, " Used: " $3, " Available: " $4, " Use%: " $5}'

}

# Function to check free memory
check_memory() {
        echo "------------------Memory Usage Details---------------------"
        free -h | awk 'NR==2{print $1, " Total: " $2, " Used: " $3, " Free: " $4, "Available: " $7}'
}

# Function Main that calls both Functions
main() {
        disk_check
        check_memory
}

# calling main fun
main
----------------------------------------------
Task 3: Strict Mode — set -euo pipefail
Create strict_demo.sh with set -euo pipefail at the top
Try using an undefined variable — what happens with set -u?
Try a command that fails — what happens with set -e?
Try a piped command where one part fails — what happens with set -o pipefail?

Document: What does each flag do?

set -e → Exit if something fails
If any command returns an error, the script stops immediately.

set -u → Error if variable is missing
If you use a variable that was never defined, the script stops with an error.

set -o pipefail → Fail if any command in a pipe fails

Normally, in a pipeline like this: command1 | command2

script -
----------------------------------
#!/usr/bin/env bash
set -euo pipefail

echo "Starting script..."

echo "1) Using undefined variable:"
echo "$undefined_var"

echo "2) Running a failing command:"
ls /not/a/real/path

echo "3) Piped command with failure:"
false | true

echo "Script finished."
--------------------------------------

What Happens?

Because set -euo pipefail is enabled:

💥 The script immediately stops with an error like:

unbound variable

👉 The script does NOT continue.

If you comment that line and run again:

🔹 With set -e (failing command)
ls /not/a/real/path

💥 ls fails → script stops immediately.

👉 The script does NOT continue.

If you comment that out too and run again:

🔹 With set -o pipefail (pipeline failure)
false | true

Normally:

true succeeds

Bash would think everything is fine

But with pipefail:
💥 The pipeline fails because false failed
→ Script stops immediately.

Task 4: Local Variables
Create local_demo.sh with:
A function that uses local keyword for variables
Show that local variables don't leak outside the function
Compare with a function that uses regular variables

Script-
---------------------------
#1 /bin/bash

echo "Using local variable iside and outside the function"

local_fun() {
        local a=12
        echo "Inside local_fun a = $a"
}

# calling local function
local_fun

echo "Outside the local_fun a = $a"

regular_fun() {
        b=2002
        echo "Inside regular fun b = $b"

}

# calling regular fun
regular_fun
echo "Outside regular fun b = $b"
--------------------------------

#! /bin/bash
set -eou pipefail

# Headline function
head_fun() {
        echo "===================================================="
        echo "SYSTEM INFORMATION REPORT"
        echo "===================================================="
}

host_os_fun() {
         echo "HOSTNAME AND OS INFO"
         echo "----------------------------------------"
        echo "Hostname : $(hostname)"
        echo "OS       : $(uname -s)"
}

print_uptime() {
    echo "UPTIME"

    uptime -p
}

print_disk_usage() {
    echo "TOP 5 DIRECTORIES BY SIZE "

    sudo df -h | sort -hr | head -n 5
 }

print_memory_usage() {
    echo "MEMORY USAGE"

    free -h
}

print_top_cpu() {
    echo "TOP 5 CPU-CONSUMING PROCESSES"

    ps -eo pid,comm,%cpu --sort=-%cpu \
        | head -n 6
}

main() {
        head_fun
        host_os_fun
         print_uptime
        print_disk_usage
        print_memory_usage
        print_top_cpu

    echo
    echo "Report Complete."
}

# calling main fun
main

what i learned 
- how to write function to reuse in scripts so that we don't have to write it repeatdly and use anythime just by calling that fun
- how to fetch data from system and how to create scripts to get system reports like memory,cpu, process, etc.
- also how to use awk in command to get only needed and usefull output
- also how to handle errors in scripts

