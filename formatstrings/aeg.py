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
    print('Pwnme')
    Pwnme(r,binary)
elif("Ret2Execve + /bin/sh" == string):
    print('ret2execve')
    Ret2Execve(r,binary)
elif("WritePrim" == string):
    print('writeprim')
    print("-----------------Here-----------------")
    WritePrim(r,binary)
elif("Ret2Win" == string):
    print('ret2win')
    Ret2Win(r,binary)
else:
    print('format_easy')
    Format_easy(binary)
