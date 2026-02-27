Day 13 – Linux Volume Management (LVM)

Task
Learn LVM to manage storage flexibly – create, extend, and mount volumes.

####  Steps ########
Creating lvm and attaching and mounting is very simple please follow the below steps.
1. create volume in aws and in same availability zone and attach to your instance
2. check the disks using df -h and lsblk
3. create physical volume
4. check physical volume using pvs or pvdisplay
5. create volume group using vgcreate
6. check vg using vgs or vgdisplay
7. create logical volume using lvcreate
8. check LVM using lvs or lvdisplay
9. format the LVM and mount to the device means dir using mkfs.ext4 and mount using mount command
10. verify the mounted lvm using df -h
11. extend the LVM using lvextend command
12. resize the lvm using resize2fs command
13. and check using df -hT


####### Comands ######
1. check disk storage - lsblk, pvs, vgs, lvs, df -h
2. create physical volume - pvcreate /dev/nvme1n1
3. check PV - pvs or pvdisplay
4. create volume group - vgcreate devops_vg /dev/nvme1n1
5. check VG - vgs or vg display
6. create LVM - lvcreate -L 500M -n app-data devops_vg
7. check LVM - lvs or lvdisplay
8. formate the LVM - mkfs.ext4 /dev/devops_vg/app-data
9. create dir to mount LVM - mkdir -p /mnt/app-data
10. munt LVM - mount /dev/devops_vg/app-data /mnt/app-data
11. extend LVM - lvextend -L +200M /dev/devops-vg/app-data
12. resize LVM - resize2fs /dev/devops_vg/app-data
13. check disk storage - df -hT

***** What you learned *******
1. setting up and creating LVM from scrach.
2. benifit of LVM flixible storage managemen and easy to resize
3. Managing disk storage
4. workflow - pV -> vf -> lv -> format -> mount -> extend

