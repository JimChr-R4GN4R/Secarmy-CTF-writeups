It's a headache to debug this piece of Powershell script . Help me out to find the output & the flag is all yours ;)

Flag Format :- secarmy{flag}

challenge.txt:


<code>
$a = "Null"
  </code>
$b = "0x00"

$c = "0x00" -in $a

$d = "null" -ge $b

$e = ($d -eq $c) -or ($a -eq $b)

$f = ($d -eq $c) -xor ($a -eq $b)

if(($d -eq $c) -or ($a -eq $b)) {$e} else {$f}
</code>

########################################

You can understand that this script can be ran at powershell compiler,so I used https://tio.run/#powershell and pasted th code there.

Output was <code>False</code> .

Flag: secarmy{False}
