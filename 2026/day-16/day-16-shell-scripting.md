Day 16 – Shell Scripting Basics
Task 1 – First Script
File: hello.sh

#!/bin/bash echo "Hello, DevOps!"

Commands: chmod +x hello.sh ./hello.sh

Observation: Script printed: Hello, DevOps!

If shebang is removed: System may not use bash interpreter properly.

Task 2 – Variables
File: variables.sh

#!/bin/bash

NAME="Hemant" ROLE="DevOps Engineer"

echo "Hello, I am $NAME and I am a $ROLE"

Single quotes vs double quotes:

Double quotes expand variables
Single quotes print text as it is
Example: echo '$NAME' Output: $NAME

echo "$NAME" Output: Hemant

Task 3 – User Input
File: greet.sh

#!/bin/bash

read -p "Enter your name: " NAME read -p "Enter your favourite tool: " TOOL

echo "Hello $NAME, your favourite tool is $TOOL"

Task 4 – If-Else
File: check_number.sh

#!/bin/bash

read -p "Enter a number: " NUM

if [ $NUM -gt 0 ]; then echo "Positive" elif [ $NUM -lt 0 ]; then echo "Negative" else echo "Zero" fi

File: file_check.sh

#!/bin/bash

read -p "Enter filename: " FILE

if [ -f "$FILE" ]; then echo "File exists" else echo "File does not exist" fi

Task 5 – Combined Script
File: server_check.sh

#!/bin/bash

SERVICE="ssh"

read -p "Do you want to check the status? (y/n): " ANSWER

if [ "$ANSWER" == "y" ]; then systemctl status $SERVICE else echo "Skipped." fi

What I Learned
Shebang defines interpreter.
Variables and read make scripts dynamic.
If-else makes automation possible.
