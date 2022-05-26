from pwn import *


for ii in range(250):
    try:
        io = process('./chal4')
        input = str(ii).encode()
        io.sendline(input)
        output = io.recvline().decode()
        print(input)
    except:
        print('Answer: ' + str(ii))
        break
print(output)

