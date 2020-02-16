My newbie scripting friend just got fooled by one of his friend and the message has been hidden using Powershell , if you help him to understand, I hope he will provide you the flag.
Warning: You might be fooled !
Flag Format:- secarmy{flag}

flag.txt: if(D642C>JL#__E6? -eq pvcure) {"flag"}

#################################################

My first thought was to try ROT decryptor.
So I gone here https://www.dcode.fr/rot-cipher and bruteforced if(D642C>JL#__E6? -eq pvcure) .

I've got these matched results:

ASCII+112	xu7SECARMY[2nnTEN/<t☺/⌂♠r♣☻t8

ASCII[!-~]+79	xu7SECARMY[2nnTEN<t"!'r&#t8

ASCII+80	↓▬Wsecarmy{R☼☼tenO\§!O &‼%"§X

ASCII[!-~]+47	:7Wsecarmy{R00ten\6BAG4FC6X


I decided to keep <code>secarmy{R00ten</code> . But what about the rest?
The I rebruteforced the <code>pvcure</code> and the best result was <code>CIPHER</code>

Flag: secarmy{R00tencipher}
