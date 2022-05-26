from qiling import *

def main():
    print("PWNME ")

    shellcode = input('>>> ').encode()
    #print(shellcode)

    if ((not shellcode.isalnum()) or (len(shellcode) > 10)):
       print("[+] Fail. Input does not meet parameters.\n")
       return

    ql = Qiling(shellcoder=shellcode,
            rootfs="qiling/examples/rootfs/x86_linux/",
            ostype="linux",
            archtype="x8664")
    #print('ql: ')
    #print(ql)
    ql.reg.rax=0x0
    ql.run()
    print('ql.reg.rax: ' + hex(ql.reg.rax))

    if (ql.reg.rax==0x41424344):
        print(open('flag.txt').readline())
    else:
        print(hex(ql.reg.rax) + ' != 0x41424344')

if __name__ == "__main__":
    try:
        main()
    except:
        print("[+] Fail. Main failed.")
