# Day 11 Challenge

## Files & Directories Created
- directory
  app-log/
  heist-project/
  bank-heist/
   heist-project/plans

-files
 devops-file.txt
 team-notes.txt
 project-config.yml
 gold.txt
 stratergy.config
 access-code.txt
 blueprints.pdf
 escape-plane.txt

## Ownership Changes
devops-file.txt
b- -rw-rw-r-- 1 ubuntu ubuntu 0 Feb 24 13:58 devops-file.txt
a- -rw-rw-r-- 1 tokyo ubuntu 0 Feb 24 13:58 devops-file.txt

team-notes.txt
b- -rw-rw-r-- 1 ubuntu ubuntu 0 Feb 24 14:03 team-notes.txt
a- -rw-rw-r-- 1 ubuntu heist-team 0 Feb 24 14:03 team-notes.txt

## Commands Used
  -touch devops-file.txt
    9  ls -l devops-file.txt 
   10  sudo useradd -m tokyo
   11  useradd -m berlin
   12  sudo useradd -m berlin
   13  sudo useradd -m professor
   14  passwd tokyo
   15  sudo passwd tokyo
   16  sudo passwd berlin
   17  sudo passwd professor 
   18  sudo chown tokyo devops-file.txt 
   19  ls -l devops-file.txt 
   20  sudo chown berlin devops-file.txt 
   21  ls -l devops-file.txt 
   22  touch team-notes.txt
   23  ls -l team-notes.txt 
   24  sudo groupadd heist-team
   25  sudo chgrp heist-team team-notes.txt 
   26  ls -l team-notes.txt 
   27  touch project-config.yml 
   28  sudo chown professor:heist-team project-config.yml 
   29  ls -l project-config.yml 
   30  mkdir app-log/
   31  ls -l app-log/
   32  ls -l app-log
   33  ls -l
   34  ls -ld app-log/
   35  sudo chown berlin:heist-team app-log/
   36  ls -ld app-log/
   37  mkdir -p heist-project/vault
   38  mkdir -p heist-project/plans
   39  touch heist-project/vault/gold.txt
   40  touch heist-project/plans/strategy.conf
   41  ls -lR heist-project/
   42  sudo chown -R professor:heist-team heist-project/
   43  ls -lR heist-project/
   44  sudo useradd -m nairobi
   45  sudo passwd nairobi 
   46  sudo groupadd vault-team, teach-team
   47  sudo groupadd vault-team
   48  sudo groupadd teach-team
   49  mkdir bank-heist/
   50  ls -ld bank-heist/
   51  touch bank-heist/access-codes.txt
   52  touch bank-heist/blueprints.pdf
   53  touch bank-heist/escape-plan.txt
   54  ls -l bank-heist/
   55  sudo chown tokyo:vault-team bank-heist/access-codes.txt 
   56  sudo chown berlin:teach-team bank-heist/blueprints.pdf 
   57  sudo chown nairobi:vault-team bank-heist/escape-plan.txt 
   58  ls -l bank-heist/

## What I Learned
- applied ownership changes across dir using recursive
- explore ownership concept and perform changes using chown command
- ownership concept in linux is imp in prodction for security purpose
