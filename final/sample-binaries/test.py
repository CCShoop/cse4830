from sddr_rop import Find_gadget

# filename = ('libc.so.6')
# print(Find_gadget.one_gadget(filename))

filename = ('libc.so.6')
filename2 = ('vuln-10')
# req = ["r12", "r13"]
op = "pop|ret"
req = ["rdi"]
gadget = Find_gadget(filename, req, op)
gadget2 = Find_gadget(filename2, req, op)
# print(gadget._file)
# print(gadget._req)
# print(gadget._op)
# print(gadget.one_gadget())

#gadget2.test()

gadget2.gadget_search()