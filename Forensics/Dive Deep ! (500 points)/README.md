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

Then chose to proceed to <code>>Disk /dev/sda</code> then <code>>\[Intel] Intel/PC partition</code>
 and then <code>>\[Analyze]</code> .
 
 Then I quicked search and chose <code>P Linux</code> and pressed <code>P</code> button to show list files.
 
 And the results gave me 2 files. The first was 'lost+found' and the second one 'Flag.zip' !
 
 So I chose 'Flag.zip' and copied it in /dev and then moved it in /root .
 
 Then I gone to forensics VM's folder (user/vmware/forensics) .
 
 And there I extracted all the data this VM had by running this command:
 
 <code>7z e forensics-disk1.vmdk</code>
 
 Then I searched in the extracted results the name 'Flag' and found the Flag.zip !
 
 Then tried to unzip it but it had a pass...
 
 So I tried to use https://www.lostmypass.com and it found the password quick enough...
 
 So the password was  <code>password</code> !
 
 So extracted the inside which was <code>flag.jpg</code> !
 
 Then tried to run it,but it could not open the file...
 
 Then wanted to confirm that it was a jpg image and run  <code>file flag.jpg</code> and the result was:
 
 <code>flag.jpg: data</code>
 
 So I opened the file with <code>hexyl flag.jpg</code> and the first line was this:
 
 <code>0e ff ff e0 00 10 4a 46 ┊ 49 46 00 01 01 00 00 01 │•×××0•JF┊IF0••00•</code>
 
 Then I opened another working jpg file and the first line was this:
  
 <code>ff d8 ff e0 00 10 4a 46 ┊ 49 46 00 01 01 01 00 48 │××××0•JF┊IF0•••0H</code>
 
 So I changed <code>0e</code> to <code>ff</code> and <code>0e</code> to <code>d8</code>
 
and the final result was:
 
<code>ff d8 ff e0 00 10 4a 46</code>

Then I opened the repaired jpg file and got a flag!

secarmy{C0ngrats_y0u_mad3_it_here}

But thos flag didn't work... :(

After some more research and anger I found this video:
https://www.youtube.com/watch?v=o1XBGsf0b0s

which shows steghide and how you can reveal the hidden data from an image.

So tried this :

<code>steghide extract -sf flag.jpg</code> and did not typed a passphrase (as like he did).

And I got surprised because the was created another file <code>flag.zip</code> which contained <code>flag.txt</code> !!!

So tried to extract it and it had also a password -_- ...

So reused https://www.lostmypass.com and got the password which is <code>123456</code> and the extracted it succesfully !!!

Flag: secarmy{th4t_w4$_3asy}

(I do not know if I will upload a video with this challenge,but if I will,then check my youtube channel https://www.youtube.com/channel/UCyvIA53elWGV95pIdmiGuGw)
