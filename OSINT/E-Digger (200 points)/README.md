Hey there , our team member just found his new domain name but I am not sure if I should email through it . Please check out .
http://umairnehri.me/
Flag Format :- secarmy {flag}

######################################################

After some time of searching and scanning, I decided to dig the site.
So I got in the terminal and typed <code>dig umairnehri.me TXT</code>
And I got this:
################################################################################

; <<>> DiG 9.11.5-P4-5.1+b1-Debian <<>> umairnehri.me TXT
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38403
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 2, ADDITIONAL: 5

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;umairnehri.me.			IN	TXT

;; ANSWER SECTION:
umairnehri.me.		1352	IN	TXT	"v=spf1 include:spf.efwd.registrar-servers.com ~all"
umairnehri.me.		1352	IN	TXT	"secarmy{$pf_r3c0rd$_@1n7_b0r1ng_r1gh7?}"

;; AUTHORITY SECTION:
umairnehri.me.		1346	IN	NS	dns1.registrar-servers.com.
umairnehri.me.		1346	IN	NS	dns2.registrar-servers.com.

;; ADDITIONAL SECTION:
dns1.registrar-servers.com. 70073 IN	A	156.154.132.200
dns1.registrar-servers.com. 405	IN	AAAA	2610:a1:1024::200
dns2.registrar-servers.com. 76674 IN	A	156.154.133.200
dns2.registrar-servers.com. 405	IN	AAAA	2610:a1:1025::200

;; Query time: 26 msec
;; SERVER: 192.168.2.1#53(192.168.2.1)
;; WHEN: Sun Feb 16 21:07:11 EST 2020
;; MSG SIZE  rcvd: 304

################################################################################

Flag: secarmy{$pf_r3c0rd$_@1n7_b0r1ng_r1gh7?}
