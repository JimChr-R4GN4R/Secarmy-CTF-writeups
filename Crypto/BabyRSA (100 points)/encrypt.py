from Crypto.Util.number import *


def make_key():
	p = getPrime(256)
	q = getPrime(256)
	n = p*q
	e = 65537
	phin = (p-1)*(q-1)
	d = inverse(e,phin)
	return n,e,d,p,q
	
n,e,d,p,q = make_key()
flag = "Screat Flag Here !!!"
print("n=",n,"p=", p)
print("ct=", pow(bytes_to_long(flag.encode()), e, n))
