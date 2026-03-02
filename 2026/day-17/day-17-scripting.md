Day 17 – Shell Scripting: Loops, Arguments & Error Handling
Task 1 – For Loop
for_loop.sh
#!/bin/bash

for fruit in apple mango banana orange grapes; do echo "Fruit: $fruit" done

count.sh
#!/bin/bash

for i in {1..10}; do echo $i done

Task 2 – While Loop
countdown.sh
#!/bin/bash

read -p "Enter a number: " NUM

while [ $NUM -ge 0 ]; do echo 
N
U
M
N
U
M
=
((NUM-1)) done

echo "Done!"

Task 3 – Command-Line Arguments
greet.sh
#!/bin/bash

if [ -z "$1" ]; then echo "Usage: ./greet.sh " exit 1 fi

echo "Hello, $1!"

args_demo.sh
#!/bin/bash

echo "Script name: 
0
"
e
c
h
o
"
T
o
t
a
l
a
r
g
u
m
e
n
t
s
:
#" echo "All arguments: $@"

Task 4 – Install Packages Script
install_packages.sh
#!/bin/bash

if [ "$EUID" -ne 0 ]; then echo "Run as root" exit 1 fi

PACKAGES="nginx curl wget"

for pkg in $PACKAGES; do if dpkg -s $pkg &> /dev/null; then echo "$pkg is already installed" else echo "Installing $pkg..." apt install -y $pkg fi done

Task 5 – Error Handling
safe_script.sh
#!/bin/bash set -e

mkdir /tmp/devops-test || echo "Directory already exists"

cd /tmp/devops-test || exit

touch test.txt

echo "File created successfully"

What I Learned
Loops make repetitive tasks automatic.
Arguments make scripts flexible.
Error handling prevents silent failures.
