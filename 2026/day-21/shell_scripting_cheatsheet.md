# Shell Scripting Cheat Sheet

## Quick Reference Table

| Topic               | Key Syntax                       | Example                                           |
| ------------------- | -------------------------------- | ------------------------------------------------- |
| Make Executable     | `chmod +x file.sh`               | `chmod +x script.sh`                              |
| Run Script          | `./file.sh`                      | `./script.sh`                                     |
| Comment             | `# comment`                      | `echo "Hi" # inline comment`                      |
| Variable            | `VAR="value"`                    | `NAME="DevOps"`                                   |
| Use Variable        | `$VAR`                           | `echo $NAME`                                      |
| Read Input          | `read VAR`                       | `read USER`                                       |
| Arguments           | `$1 $2 $# $@ $?`                 | `./script.sh arg1`                                |
| String Compare      | `[ "$a" = "$b" ]`                | `[ "$name" = "Linux" ]`                           |
| Integer Compare     | `[ $a -gt 10 ]`                  | `[ $num -eq 5 ]`                                  |
| File Test           | `[ -f file ]`                    | `[ -d /home ]`                                    |
| If Condition        | `if [ cond ]; then`              | `if [ -f file ]; then echo OK; fi`                |
| Case Statement      | `case $v in ... esac`            | `case $1 in start) echo run ;; esac`              |
| AND                 | `cmd1 && cmd2`                   | `mkdir test && cd test`                           |
| OR                  | `cmd1 \|\| cmd2`                 | `cd dir \|\| pwd`                                 |
| For Loop            | `for i in list; do`              | `for i in 1 2 3; do echo $i; done`                |
| C-Style For         | `for ((i=1;i<=3;i++))`           | `for ((i=1;i<=3;i++)); do touch f$i; done`        |
| While Loop          | `while [ cond ]; do`             | `while [ $a -lt 5 ]; do echo $a; done`            |
| Until Loop          | `until [ cond ]; do`             | `until ping -c1 google.com; do sleep 2; done`     |
| Break               | `break`                          | `if [ $i -eq 5 ]; then break; fi`                 |
| Continue            | `continue`                       | `if [ $i -eq 2 ]; then continue; fi`              |
| Function            | `name() { ... }`                 | `greet(){ echo "Hi"; }`                           |
| Function Arg        | `$1 inside function`             | `add(){ echo $(($1+$2)); }`                       |
| Return Status       | `return 0`                       | `return 1`                                        |
| Capture Output      | `result=$(func)`                 | `val=$(date)`                                     |
| Local Variable      | `local var=value`                | `local count=10`                                  |
| grep                | `grep pattern file`              | `grep -i "error" log.txt`                         |
| awk                 | `awk '{print $1}' file`          | `awk -F: '{print $1}' /etc/passwd`                |
| sed                 | `sed 's/a/b/g' file`             | `sed -i 's/foo/bar/g' file.txt`                   |
| cut                 | `cut -d: -f1 file`               | `cut -d: -f1 /etc/passwd`                         |
| sort                | `sort file`                      | `sort -n numbers.txt`                             |
| uniq                | `sort file \| uniq`              | `sort file \| uniq -c`                            |
| tr                  | `tr 'a-z' 'A-Z'`                 | `echo hi \| tr 'a-z' 'A-Z'`                       |
| wc                  | `wc -l file`                     | `wc -w file.txt`                                  |
| head                | `head -n 5 file`                 | `head -n 10 log.txt`                              |
| tail                | `tail -f file`                   | `tail -f app.log`                                 |

---

## 1. Basics

### Shebang (`#!/bin/bash`)
- **What it does**: Tells the system to use `/bin/bash` interpreter to execute the script.
- **Why it matters**: Without it, the script runs with the default shell, which may cause compatibility issues.
- **Example**:
  ```bash
  #!/bin/bash
  echo "Hello, world!"
Running a script
chmod +x script.sh – Make the script executable.

./script.sh – Run the script (uses shebang).

bash script.sh – Run the script explicitly with Bash (ignores shebang).

Comments
Single line: # This is a comment

Inline: echo "Hello" # prints Hello

Comments are ignored by the shell but essential for code readability.

Variables
Declaring: NAME="John" (no spaces around =).

Using: $NAME or ${NAME}.

Quoting:

Double quotes: "Hello $NAME" → expands variable.

Single quotes: 'Hello $NAME' → literal string.

Reading user input
read – Reads input into a variable.

Example:

bash
echo "Enter your name:"
read NAME
echo "Hello $NAME!"
Command-line arguments
$0 – Script name.

$1, $2, ... – Positional arguments.

$# – Number of arguments.

$@ – All arguments as separate words.

$? – Exit status of last command.

Example:

bash
#!/bin/bash
echo "Script: $0"
echo "First arg: $1"
echo "Total args: $#"
echo "All args: $@"

ls /nonexistent
echo "Exit status: $?"   # non-zero indicates failure
2. Operators and Conditionals
String comparisons
Operator	Meaning	Example
=	Equal	[ "$a" = "$b" ]
!=	Not equal	[ "$a" != "$b" ]
-z	Zero length (empty)	[ -z "$str" ]
-n	Non-zero length	[ -n "$str" ]
Integer comparisons
Operator	Meaning	Example
-eq	Equal	[ $a -eq $b ]
-ne	Not equal	[ $a -ne $b ]
-lt	Less than	[ $a -lt $b ]
-gt	Greater than	[ $a -gt $b ]
-le	Less or equal	[ $a -le $b ]
-ge	Greater or equal	[ $a -ge $b ]
File test operators
Operator	Meaning	Example
-f	Regular file exists	[ -f file ]
-d	Directory exists	[ -d dir ]
-e	File/directory exists	[ -e path ]
-r	Readable	[ -r file ]
-w	Writable	[ -w file ]
-x	Executable	[ -x file ]
-s	Non-empty file	[ -s file ]
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
&& – AND: [ cond1 ] && [ cond2 ]

|| – OR: [ cond1 ] || [ cond2 ]

! – NOT: ! [ cond ]

Case statements
bash
case $VAR in
  pattern1)
    commands ;;
  pattern2|pattern3)
    commands ;;
  *)
    default commands ;;
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
break – Exit the loop.

continue – Skip to next iteration.

Looping over files
bash
for file in *.log; do
  echo "Processing $file"
done
Looping over command output (while read)
bash
ls *.txt | while read line; do
  echo "File: $line"
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
Passing arguments to functions
Inside the function, $1, $2, etc. refer to function arguments.

bash
greet() {
  echo "Hello, $1"
}
greet "World"
Return values
return – Returns an exit status (0–255). Capture with $?.

echo – Outputs data that can be captured with command substitution.

Example:

bash
# Using return for status
check_file() {
  if [ -f "$1" ]; then
    return 0
  else
    return 1
  fi
}
check_file "/etc/passwd" && echo "Exists"

# Using echo for value
get_date() {
  echo "$(date +%Y-%m-%d)"
}
today=$(get_date)
Local variables
local – Declare a variable local to the function.

Example:

bash
myfunc() {
  local count=5
  echo "Inside: $count"
}
myfunc
echo "Outside: $count"   # empty
5. Text Processing Commands
grep – search patterns
bash
grep -i "error" log.txt          # case-insensitive
grep -r "TODO" .                  # recursive
grep -c "failed" auth.log         # count matches
grep -n "sshd" /etc/ssh/sshd_config  # show line numbers
grep -v "INFO" syslog              # invert match
grep -E "error|warn" log.txt       # extended regex
awk – column-based processing
bash
awk '{print $1}' file              # print first column
awk -F: '{print $1, $3}' /etc/passwd   # delimiter :
awk '/root/ {print $1}' file        # pattern match
awk 'BEGIN{print "Start"} {print} END{print "End"}' file
sed – stream editor
bash
sed 's/old/new/g' file             # substitute all occurrences
sed -i 's/old/new/g' file          # in-place edit
sed '/pattern/d' file               # delete matching lines
sed '2d' file                       # delete line 2
sed -n '10,20p' file                # print lines 10-20
cut – extract columns by delimiter
bash
cut -d: -f1 /etc/passwd            # first field using :
cut -d',' -f2,4 data.csv           # fields 2 and 4
cut -c1-10 file                     # first 10 characters
sort – sort lines
bash
sort file                          # alphabetical
sort -n file                       # numerical
sort -r file                       # reverse
sort -u file                       # unique (same as uniq)
sort -k2 -t: file                  # sort by field 2 with delimiter :
uniq – deduplicate lines (input must be sorted)
bash
sort file | uniq                   # global unique
sort file | uniq -c                # count occurrences
uniq -u file                       # show only unique lines
tr – translate/delete characters
bash
echo "hello" | tr 'a-z' 'A-Z'      # uppercase
echo "hello 123" | tr -d '0-9'     # delete digits
tr -s ' ' < file                    # squeeze spaces
wc – line/word/char count
bash
wc -l file                         # line count
wc -w file                         # word count
wc -c file                         # character count
head / tail – first/last lines
bash
head -n 5 file                     # first 5 lines
tail -n 20 file                    # last 20 lines
tail -f log.txt                    # follow live updates
6. Useful Patterns and One-Liners
Find and delete files older than N days
bash
find /var/log -type f -name "*.log" -mtime +15 -delete
Count lines in all .log files
bash
wc -l /var/log/*.log | tail -1
Replace a string across multiple files
bash
sed -i 's/db.oldserver.com/db.newserver.com/g' /etc/myapp/*.conf
Check if a service is running
bash
systemctl is-active --quiet nginx && echo "Running" || echo "Stopped"
Monitor disk usage with alert
bash
df -h | awk '$5+0 > 80 {print $0}' | mail -s "Disk Alert" admin@example.com
Tail a log and filter for errors in real time
bash
tail -f /var/log/syslog | grep --line-buffered -E 'ERROR|CRITICAL'
Parse CSV (simple)
bash
awk -F',' '{print $1}' data.csv
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

exit 1 – General error (or any non-zero value).

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
trap – Execute code on script exit or signal.
bash
cleanup() {
  rm -f /tmp/tempfile
}
trap cleanup EXIT

