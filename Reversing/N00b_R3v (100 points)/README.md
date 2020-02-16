Just Debug It >3
Flag Format ; secarmy{flag}

file: debug
################################

After downloading it, I tried to open it with ollydbg but it could not load it,so typed in terminal <code>file debug</code> and I got that it is a ELF file.

So typed <code>strings debug</code> and got this:

<code>
secarmy{n00b_rev3rs3r}
.shstrtab
.text
.data
.bss
</code>

Flag: secarmy{n00b_rev3rs3r}
