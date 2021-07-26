# ca.key
if lu got file ca.key
bisa bikin file server.csr dengan openssl untuk bikin cert

    openssl req -new -key ca.key -out server.csr

lalu generate keynya

    openssl x509 -req -days 365 -in server.csr -signkey ca.key -out server.crt 

terakhir buat file PKCS12 cert nya

    openssl pkcs12 -export -in server.crt -inkey ca.key -out server.p12

lalu import di browser