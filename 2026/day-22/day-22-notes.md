Day 22 – Introduction to Git: Your First Repository

What is the difference between git add and git commit?
- git add stagged the untracked file or changes and git commit tracked the stagged changes and save into git repo with message.

What does the staging area do? Why doesn't Git just commit directly?
- The staging area lets you choose exactly which changes to include in the next commit.
Why Git uses it:
You can organize commits better
You can commit only some files or parts of files
Example:
You changed 5 files but only want to commit 2 → stage those 2.

What information does git log show you?
- git logs shows all the commit you have made in repo all changes you made and commit history.

What is the .git/ folder and what happens if you delete it?
- .git folder store all git project data and if you delete it project stoped being git repo and all commit history will be deleted.

What is the difference between a working directory, staging area, and repository?
- Part	                Meaning
Working Directory	- Your actual project files where you edit code
Staging Area	- Place where you prepare changes before committing
Repository	- Where Git permanently stores commits
