Shell Scripting Cheat Sheet

Quick Reference Table

Topic	Key Syntax	Example
Shebang	#!/bin/bash	#!/bin/bash
Variable	VAR="value"	NAME="DevOps"
Argument	$1, $2	./script.sh arg1
If	if [ condition ]; then	if [ -f file ]; then
For loop	for i in list; do	for i in 1 2 3; do
Function	name() { ... }	greet() { echo "Hi"; }
Grep	grep pattern file	grep -i "error" log.txt
Awk	awk '{print $1}' file	awk -F: '{print $1}' /etc/passwd
Sed	sed 's/old/new/g' file	sed -i 's/foo/bar/g' config.txt
Cut	cut -d',' -f1 file	cut -d: -f1 /etc/passwd
Sort	sort -n -r file	sort -k2 -t: file
Uniq	uniq -c	sort file | uniq -c
Find	find path -name pattern	find . -name "*.log" -mtime +7 -delete
Exit code	$?	if [ $? -eq 0 ]; then

1. Basics
Shebang
#!/bin/bash – Specifies the interpreter to execute the script. Must be the first line.

Running a script
chmod +x script.sh – Make script executable.

./script.sh – Execute script (requires execute permission).

bash script.sh – Run script with bash interpreter (ignore shebang).

Comments
Single line – # This is a comment

Inline – command # comment after command

Variables
Declaring – NAME="John" (no spaces around =)

Using – $NAME or ${NAME}

Quoting:

"$VAR" – Expands variable, preserves spaces.

'$VAR' – Literal string, no expansion.

Reading user input
read – Read input into variable.

bash
echo "Enter your name:"
read NAME
echo "Hello $NAME"
Command-line arguments
$0 – Script name.

$1, $2, ... – Positional arguments.

$# – Number of arguments.

$@ – All arguments as separate words.

$? – Exit status of last command.

2. Operators and Conditionals
String comparisons
Operator	Meaning	Example
=	Equal	[ "$a" = "$b" ]
!=	Not equal	[ "$a" != "$b" ]
-z	String is empty (zero length)	[ -z "$a" ]
-n	String is not empty	[ -n "$a" ]
Integer comparisons
Operator	Meaning	Example
-eq	Equal	[ $a -eq $b ]
-ne	Not equal	[ $a -ne $b ]
-lt	Less than	[ $a -lt $b ]
-gt	Greater than	[ $a -gt $b ]
-le	Less than or equal	[ $a -le $b ]
-ge	Greater than or equal	[ $a -ge $b ]
File test operators
Operator	Meaning	Example
-f	File exists and is regular	[ -f file ]
-d	Directory exists	[ -d dir ]
-e	File/directory exists	[ -e path ]
-r	Readable	[ -r file ]
-w	Writable	[ -w file ]
-x	Executable	[ -x file ]
-s	File exists and not empty	[ -s file ]
if, elif, else syntax
bash
if [ condition ]; then
  # commands
elif [ condition2 ]; then
  # commands
else
  # commands
fi
Logical operators
&& – AND: [ condition1 ] && [ condition2 ]

|| – OR: [ condition1 ] || [ condition2 ]

! – NOT: [ ! condition ]

Case statements
bash
case $VAR in
  pattern1)
    commands;;
  pattern2|pattern3)
    commands;;
  *)
    default commands;;
esac
3. Loops
for loop (list-based)
bash
for i in 1 2 3; do
  echo $i
done
for loop (C-style)
bash
for (( i=0; i<5; i++ )); do
  echo $i
done
while loop
bash
count=1
while [ $count -le 5 ]; do
  echo $count
  ((count++))
done
until loop
bash
count=1
until [ $count -gt 5 ]; do
  echo $count
  ((count++))
done
Loop control
break – Exit loop.

continue – Skip to next iteration.

Looping over files
bash
for file in *.log; do
  echo "Processing $file"
done
Looping over command output (while read)
bash
cat file.txt | while read line; do
  echo $line
done
4. Functions
Defining a function
bash
function_name() {
  # commands
}
Calling a function
bash
function_name
Passing arguments
Inside function: $1, $2, $@ refer to function arguments, not script arguments.

bash
greet() {
  echo "Hello $1"
}
greet "World"
Return values
return – Exit function with exit status (0-255).

echo – Output data to be captured.

bash
get_name() {
  echo "John"
}
NAME=$(get_name)
Local variables
local – Declare variable local to function.

bash
myfunc() {
  local VAR="local"
  echo $VAR
}
5. Text Processing Commands
grep – search patterns
bash
grep "pattern" file               # basic search
grep -i "error" log.txt           # case-insensitive
grep -r "TODO" .                  # recursive
grep -c "error" log.txt           # count matches
grep -n "error" log.txt           # show line numbers
grep -v "exclude" file            # invert match
grep -E "err|warn" log.txt        # extended regex (or)
awk – column-based processing
bash
awk '{print $1}' file             # print first column
awk -F: '{print $1}' /etc/passwd  # field separator :
awk '$2 > 100 {print $1}' file    # condition on column 2
awk 'BEGIN{print "Start"} {print} END{print "End"}' file
sed – stream editor
bash
sed 's/old/new/g' file            # substitute all occurrences
sed -i 's/old/new/g' file         # in-place edit
sed '/pattern/d' file              # delete lines matching pattern
sed '5d' file                      # delete line 5
sed -n '10,20p' file               # print lines 10-20
cut – extract columns
bash
cut -d',' -f1,3 file.csv          # delimiter , fields 1 and 3
cut -c1-10 file                    # characters 1-10
cut -d: -f1 /etc/passwd            # first field using :
sort – sort lines
bash
sort file                          # alphabetical
sort -n file                       # numerical
sort -r file                       # reverse
sort -u file                       # unique (like uniq)
sort -k2 -t: file                  # sort by field 2 with delimiter :
uniq – unique lines (requires sorted input)
bash
uniq file                          # remove consecutive duplicates
sort file | uniq                   # global unique
sort file | uniq -c                # count occurrences
tr – translate/delete characters
bash
tr '[:lower:]' '[:upper:]' < file  # uppercase
tr -d ',' < file                    # delete commas
tr -s ' ' < file                    # squeeze spaces
wc – word/line/character count
bash
wc -l file                          # line count
wc -w file                          # word count
wc -c file                          # byte count
head / tail – first/last lines
bash
head -n 10 file                     # first 10 lines
tail -n 20 file                     # last 20 lines
tail -f log.txt                     # follow file (live)
6. Useful Patterns and One-Liners
Find and delete files older than N days
bash
find /path -type f -name "*.log" -mtime +7 -delete
Count lines in all .log files
bash
wc -l *.log | tail -1               # total lines
Replace a string across multiple files
bash
sed -i 's/old/new/g' *.txt
Check if a service is running
bash
systemctl is-active --quiet service && echo "Running" || echo "Stopped"
Monitor disk usage with alert
bash
df -h | awk '$5+0 > 80 {print "Alert: " $6 " is " $5 " full"}'
Parse CSV (simple)
bash
awk -F',' '{print $1}' file.csv
Tail a log and filter errors in real time
bash
tail -f app.log | grep --line-buffered "ERROR"
Get IP address of a domain
bash
dig +short example.com
Find largest files in directory
bash
find . -type f -exec du -h {} + | sort -rh | head -10
Kill all processes matching name
bash
pkill -f "process_name"
7. Error Handling and Debugging
Exit codes
$? – Exit status of last command.

exit 0 – Success.

exit 1 – General error.

set -e – Exit script on any error.
bash
set -e
set -u – Treat unset variables as error.
bash
set -u
set -o pipefail – Catch errors in pipes.
bash
set -o pipefail
set -x – Debug mode (print commands and arguments).
bash
set -x
trap – Catch signals and execute cleanup.
bash
trap 'echo "Interrupted"; exit' INT
trap 'rm -f /tmp/tmpfile' EXIT   # cleanup on script exit
