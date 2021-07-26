# cek windows security patch

    systeminfo

# cek priv

    whoami /priv

# cek local service

    netstat -ano | findstr TCP | findstr ":0"

# cek process

    tasklist /v | findstr 2820

# Enum4linux

    enum4linux -a 10.10.10.100
