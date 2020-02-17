Are you good at forensics? can we test you ?

Dive in :- https://drive.google.com/file/d/1gVnPf5axFovFcl-arFZu39dE-qsDmR5s/view?usp=sharing

extract the real flag, its easy.

Flag Format : secarmy{}

#################################################

Downloaded the file with name forensics.ova and run it in vmware. Then it says to login, so put default username <code>root</code> and password <code>toor</code> and got in!

Then typed <code>ls</code> to check what files do I have and I got this result:

flag.jpg , flag.txt , Readme.txt

So I cat flag.txt and got this result: <code>c2VjYXJteXtmbGFnfQ==</code> 

which is base64 encoded,so decoded it and got <code>secarmy{flag}</code>

This is not the flag... So let's check Readme.txt

<code>cat Readme.txt</code> and got this result:

Is your forensics really good???

can you find the actual flag,

dig in very deep!!!

So I thinked to search deeper.After some time I thinked to check for any corrupt or generally recoverable files in /dev/sda.

So after some research used <code>testdisk /dev/sda</code>

Then chose to proceed to <code>>Disk /dev/sda</code> and then <code>>\[Intel] Intel/PC partition</code>
