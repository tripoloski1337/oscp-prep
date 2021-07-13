# Tunneling with chisel

download exec disini: `https://github.com/jpillora/chisel/releases/tag/v1.7.6`

# Run server  

jalankan server di local dengan cara

    ./chisel server -p 8000 --reverse

# Run client

jalankan client di target dengan cara

    .\chisel.exe client 10.10.14.22:8000 R:8888:localhost:8888

fyi, portnya 8888 itu service yang ada di mesin target jalan di port 8888

# test koneksi

coba koneksi dengan perintah:

    ┌──(tripoloski㉿kali)-[~/oscp/htb/buff]
    └─$ netstat -tlpn
    (Not all processes could be identified, non-owned process info
    will not be shown, you would have to be root to see it all.)
    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 10.10.14.22:80          0.0.0.0:*               LISTEN      -
    tcp        0      0 10.10.14.22:81          0.0.0.0:*               LISTEN      -
    tcp        0      0 10.10.14.22:82          0.0.0.0:*               LISTEN      -
    tcp        0      0 10.10.14.22:84          0.0.0.0:*               LISTEN      -
    tcp6       0      0 :::8000                 :::*                    LISTEN      54495/./chisel
    tcp6       0      0 :::8888                 :::*                    LISTEN      54495/./chisel