# Cracking Drupal 7 password with john

john --format=Drupal7 -wordlist=../../tools/wordlist/rockyou.txt ./hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Drupal7, $S$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 32768 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
booboo           (?)
1g 0:00:00:00 DONE (2021-04-28 12:59) 2.380g/s 552.3p/s 552.3c/s 552.3C/s tiffany..harley
Use the "--show" option to display all of the cracked passwords reliably
Session completed
