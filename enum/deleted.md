# recover deleted file from linux

kalo file tersebut dihapus dan ada pada /dev/sdb or /dev/sdX
bisa pakai perintah: 
    
    cat /dev/sdbX 

untuk liat isi file deleted, atau bisa juga dengan:

    grep –binary-files=text –context=100 ‘root’ /dev/sdb > /tmp/root.txt
    