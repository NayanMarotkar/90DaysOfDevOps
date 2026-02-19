07 day Practice notes.

 Linux File System Hierarchy = The linux filesystem hierarchy is a tree like structure starts from top which is root dir which is represented by / and all dir starts from /
 this structure is defined by the FHS (Filesystem Hierarchy Standard) and organize all files and devices in system.
    There are some important dir's you must know and have knowledge about tem and what they store and use for.

1. / - It is a home dir of root user and also starting point of everything.
2. /etc - it is used to store config. files (resources).
3. /usr - user related files are stored here.
4. /opt - use for add on services.
5. /bin - stores binary executable filed and it's commands.
6. /sbin - it stores binary executable files and ts comands of root user. It can not be executed by local user.
7. /boot - it is used to store bootloader related files.
8. /home - it is a home dir of local user.
9. /dev - it stores devices and blockage files.
10. /var - it stores variable data such as email, meaasge, logs etc.
11. /mnt - standard dir for mounting storage devices.
12. /lib - it stores library files it supports 32-bit.
13. /lib64 - it stores 64-bit library files.
14. /tmp - it stores temperory files.

Part 2: Scenario-Based Practice (40 minutes)
Important: Focus on understanding the troubleshooting flow, not memorizing commands. Use the hints!

Scenario 1: Service Not Starting

A web application service called 'myapp' failed to start after a server reboot.
What commands would you run to diagnose the issue?
Write at least 4 commands in order.

ans - 1. check if service is running or not using "systemctl status myapp"
         why - using systemctl status command you can check the servies current state like it is running or not.
      2. then check the logs of service using "journalctl -u myapp -n 50"
          why - using this commmad you can check all the log event of that service from starting to how it initialize and where error occur.
      3. check is it enable to start on boot "systemctl is-enabled myapp"
      why - usig this command you can check if service is enable to start on boot or not you will get output like = enabled.

Scenario 2: High CPU UsageScenario 

Your manager reports that the application server is slow.
You SSH into the server. What commands would you run to identify
which process is using high CPU?

ans - 1. use "top" command
       why - will list all running processes in realtime and you can check which process is using high resources.
      2. use "ps aux --sort=-%cpu | head -10" command.
      why - it will sort process by cpu percentage.
      3. note PID of process using high cpu.
       why - if you need to kill that process you can kill using command sudo kill -9 PID.

Scenario 3: Finding Service Logs

A developer asks: "Where are the logs for the 'docker' service?"
The service is managed by systemd.
What commands would you use?

ans - 1. systemctl status docker
      why - check if the service is running or not.
      2. journalctl -u docker -n 50
    why - you can check its logs events and check if there is any errors.
     3. journalctl -u ssh -f
    whhy - you can see services logs in realtime 

Scenario 4: File Permissions Issue

A script at /home/user/backup.sh is not executing.
When you run it: ./backup.sh
You get: "Permission denied"
What commands would you use to fix this?

ans - 1. ls -l
    why - check the permission of file using this command.
    2. chmod +x /home/user/backup.sh
    why - t execute script file should have execute permission whuch is shown as "x".
    3. ls -l /home/user/backup.sh
     why - verify that permission is now set or not 
    4.  ./backup.sh
    - run the script.

  
