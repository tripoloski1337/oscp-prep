# SCANNING WITH NMAP 

sudo nmap -sC -sV -vv 10.10.10.229 


# Kalo gabisa konek + gaada port open 

    nmap -p 21,22,139,445,3632 -sV -sC -oA scans/tcpscripts <host>

# Scan SMB vuln

    nmap --script smb-vuln* -p 445 10.10.10.40 