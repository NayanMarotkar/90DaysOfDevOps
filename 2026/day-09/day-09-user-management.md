# Day 09 Challenge

## Users & Groups Created
- Users: tokyo, berlin, professor, nairobi
- Groups: developers, admins, project-team

## Group Assignments
- tokyo → developers
- berlin → developers + admins (both groups)
- professor → admins

## Directories Created
- /op/dev-project
- /opt/team-workspace

## Commands Used

- user create
   sudo useradd -m <username>

-set password for user
 sudo passwd <username>

- verify created user
   grep -e tokyo -e berlin -e professor /etc/passwd

- listing dir and files
   ls -l

- adding user into group
    sudo usermod -aG developers tokyo

- checking user is added in which groups
  groups berlin

- changing dirs group owner
  sudo chgrp developers /opt/dev-project/

- changing file permissions
   sudo chmod 775 /opt/team-workspace

  ## What I Learned
  - always check in which dir you are currently
  - some commands are not run by local users root permission are needed
  - when creating file in production give exact permission needed to correct user and group
  - always verify the changes you make in dir or files
    
 
