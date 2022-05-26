from pwn import *
from Identify import *
from easy_format import *
#binaries = [['   Name','SOF','Win','Sys','Bin','scall','Execve','Pwn','Gadget']]
#binary = ['isSOF', 'isWin', 'isSystem', 'isBinSh', 'syscall', 'isExecve', 'isPwnme']
		
binary = context.binary = ELF(args.BIN)
r = ROP(binary)

curBinary = Identify(binary,r)
string = AttackVector(curBinary)
print(curBinary)
#curBinary.append(string)
#binaries.append(curBinary)

if("Pwnme" == string):
	Pwnme(r,binary)
elif("Ret2Execve + /bin/sh" == string):
	Ret2Execve(r,binary)
elif("WritePrim" == string):
	print("-----------------Here-----------------")
	WritePrim(r,binary)
elif("Ret2Win" == string):
	Ret2Win(r,binary)
else:
	Format_easy(binary)