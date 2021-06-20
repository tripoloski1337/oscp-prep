# find badchar pake mona, nanti ada file bytearray.bin disana

    !mona bytearray


# find badcharnya 

    !mona compare -f bytearray.bin  -a <017DFA30 ini address yang nyimpen input pertama>


# mona buat remove badchar, kalo kebanyakan atau shellcode gajalan
pakai cara ini

    !mona bytearray -b "\x00\x23\x3c"

-b itu buat badcharnya
