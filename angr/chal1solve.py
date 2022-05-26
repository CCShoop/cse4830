import angr

p = angr.Project('./chal1')

goal = 0x125f +0x400000
start_addr = 0x1214 +0x400000
state = p.factory.entry_state(addr=start_addr)
simgr = p.factory.simgr(state)
simgr.explore(find=goal)
stdin = simgr.found[0].posix.dumps(0)
print("solve is {}".format(stdin))
print(simgr.found[0].posix.dumps(1))

