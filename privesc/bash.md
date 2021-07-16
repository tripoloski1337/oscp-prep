# suid bash

    Running SUDO permission without a password

    User www-data may run the following commands on bashed:
        (scriptmanager : scriptmanager) NOPASSWD: ALL


    In this example as this is a user not a file, we can execute as user "scriptmanager"
    without specifying a password.


    www-data@bashed:/dev/shm$ sudo -u scriptmanager /bin/bash