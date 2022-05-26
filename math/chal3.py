from pwn import *


for ii in range(250):
    io = process('./chal3')
    input = str(ii).encode()
    io.sendline(input)
    output = io.recvline().decode()
    print(input)
    print(output)

