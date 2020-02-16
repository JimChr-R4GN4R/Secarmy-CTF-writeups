Hey , hope your basics are pretty clear.
Flag Format:- secarmy{flag}

RSA.7zip : data.txt,encrypt.py (you can find them in this folder)

#################################################

So from data.txt we have n,p and ciphertext and from encrypt.py file we have e=65537 . So I can find q=n/p , phi = (p - 1) * (q - 1) and d.So we have them all BUT.
I have made a script for this RSA situation from picoCTF 2019!
You can find it here:
https://github.com/JimChr-R4GN4R/picoCTF-writeups/blob/master/2019/Cryptography/rsa-pop-quiz%20(200%20points)/p-ct-e-n-_q-_phi-_d_pl.py

So just pasted in it the values and got the flag just like that!

Flag: secarmy{Y0uR_R$@_B@S!c_!$_CLe3r}
