# cracking shadow solaris

    hashcat -m 7400 hash ~/oscp/tools/wordlist/rockyou.txt --force

# cracking kerberos 

    hashcat -m 13100 -a 0 GetUserSPNs.out ~/oscp/tools/wordlist/rockyou.txt --force

