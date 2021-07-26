# SMBD client liat share

    smbclient --list //10.10.10.134/ -U ""

# SMB liat dir

    smbclient //10.10.10.134/Backups -U ""

# SMB cliant 

    smbclient //10.10.10.100/Replication -U "%"

# Mount SMB vhd to /mnt

    root@kali:~/Desktop/HTB/boxes/bastion# mkdir /mnt/L4mpje-PC
    root@kali:~/Desktop/HTB/boxes/bastion# mkdir /mnt/vhd
    root@kali:~/Desktop/HTB/boxes/bastion# modprobe nbd
    root@kali:~/Desktop/HTB/boxes/bastion# mount -t cifs //bastion.htb/Backups/WindowsImageBackup/L4mpje-PC  /mnt/L4mpje-PC/ -o user=anonymous
    Password for anonymous@//bastion.htb/Backups/WindowsImageBackup/L4mpje-PC:
    root@kali:~/Desktop/HTB/boxes/bastion# qemu-nbd -r -c /dev/nbd0 "/mnt/L4mpje-PC/Backup 2019-02-22 124351/9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd"
    root@kali:~/Desktop/HTB/boxes/bastion# mount -r /dev/nbd0p1 /mnt/vhd
    root@kali:~/Desktop/HTB/boxes/bastion#

