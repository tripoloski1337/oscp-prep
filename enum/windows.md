# cek windows security patch

    systeminfo

# cek priv

    whoami /priv

# cek local service

    netstat -ano | findstr TCP | findstr ":0"

# cek process

    tasklist /v | findstr 2820