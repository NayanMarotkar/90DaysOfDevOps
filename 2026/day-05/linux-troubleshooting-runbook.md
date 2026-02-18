Troubleshooting using docker service -

1. using top command we can check all info related that service in realtime like cpu memory etc and if you only want to output related that system other then all system and process
2. you can use command like  - top -b -n 1 | grep docker in this -b means bach mode and -n stands for how many literation you need and with grep you cn find info about specific service.

you can check dick space of all dir using df -hT and you can check which folder or file in specific dir or specific fir is occupying spce using du -sh command.

you can use journalctl -u service name to check all logs related that service what events happend in it from start end and you can see that your in your system all services are in
healthy state and its disk usage you can use free -h command to check free resources and used resources.

