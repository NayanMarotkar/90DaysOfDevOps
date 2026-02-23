# Day 10 Challenge
File Permissions & File Operations Challenge

## Files Created
- devops.txt
- notes.txt
- script.sh
  
## Permission Changes
  files           before     after  
 -devops.txt        644      444
- notes.txt         644      640
- script.sh         644      755

## Commands Used
-create file
  touch <file-name>

- write in files
  vim, echo

- modify permission of files
   sudo chmod 755 <file-name>

- check first five lines
  head -n 5 filename

- check last five lines in file
  tail -n 5 filename

- create dir
  mkdir dirname

-Try writing to a read-only file - what happens?
 ans - -bash: devops.txt: Permission denied getting this error that the permission is denied

-Try executing a file without execute permission
 ans - -bash: ./script.sh: Permission denied it says that we don't have required permission
  
## What I Learned
- when you are giving permission to the files or dir always give the least previlage
- when we execute any script we need the executable permission to run that script
- understanding how to fix permission error
- understand how to manage files permission 
