The hashtag hint :- #wearesecarmy

Flag Format:- secarmy{flag}

#################################

When read the description my first thought was to use a scraper...

So I started with Instagram. I have made a scraper in python for my University 

https://github.com/JimChr-R4GN4R/Python_University_Projects/tree/master/Askhsh_6 (We love Patsakis <3)

so I used it to scrape Instagram posts with the hashtag '#wearesecarmy' by typing:

<code>python3 scraper.py --comments --tag wearesecarmy</code>


So,when finished,I got in .json file which has the comments etc and searched for 'secarmy{' and the first thing I got was this:

"text": "<code>secarmy{Clear_The_Snow}</code>\\n\\nCame across....

So copied <code>secarmy{Clear_The_Snow}</code>

But this wasn't the flag...

So searched for others and found this line:

"text": "‪ ‪How we ranked 4th in SHELL-CTF 0x01 (Writeup)‬ Link: link.medium.com/eIXJPf1LfU‬\\n\\n<code>secarmy{w3_actUalLy</code>\\n\\n#shell #ctf #hackers #cybersecurity #mrrobot #challenges #winner #wearesecarmy"

So copied that: secarmy{w3_actUalLy

and tried to find the other half.

Searched '}\\n' (because the first flag we found is ending with }\\n) and found this:

"text": "Video: @thehackingsage \\nLines: @_navneetmuffin_ \\n<code>_n0t_1337s}</code>\\n#hacker

So copied <code>_n0t_1337s}</code> and finally we got the flag!

Flag: secarmy{w3_actUalLy_n0t_1337s}
