from pwn import *
from binascii import *
context.update(arch='amd64', os='linux')
context.log_level = 'critical'

def assemble():
    a='6a6848b82f62696e2f2f2f73504889e768726901018134240101010131f6566a085e4801e656'
    b = input('setup the registers for execve >>> ')
    c='6a3b580f05'

    shell=unhexlify(a+b+c)
    p=run_shellcode(shell)
    p.sendline(b'cat flag.txt')
    print(p.recv())

def main():
    print("\n")
    assemble()

if __name__ == "__main__":
    main()
