Life is although void , but SECARMY can help you out , hope you get it >3.

Flag Format:- secarmy{flag}

flag.txt: 

<code>42 ds24 ds44 ds30 ds28 ds70 ds110 ds66 ds43 ds34 ds48 ds26 ds90 ds100 ds63 ds55 ds64 ds47 ds55 ds80 ds76</code>

################################################################

So at first tried to identify the cipher which has been used,but found nothing at the beginning.

Then saw that the first number has no 'ds', so tried to remove ds from all the text.

<code>42 24 44 30 28 70 110 66 43 34 48 26 90 100 63 55 64 47 55 80 76</code>

Then my first thought was that he used Polybious square, but tried it and got no result... :(

Then searched similar ciphers on duckduckgo and found this on wikipedia https://en.wikipedia.org/wiki/Polybius_square:

Polybius square: ADFGVX, Bifid, Nihilist, Tap, code, Trifid, VIC cipher

- ADFGVX and Bifid uses alphabet so ignored

Then checked about Nihilist decoder and chose https://cryptii.com/pipes/nihilist-cipher to decrypt it with separator the space.

But it needed a key... So checked description one more time and tried SECARMY as a key and it worked!

Flag: secarmy{thekeytopoints}
