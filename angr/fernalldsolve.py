import angr

p = angr.Project('./fernalld')

goal = 0x1464 +0x400000
start_addr = 0x14da +0x400000
state = p.factory.entry_state(addr=start_addr)
simgr = p.factory.simgr(state)
simgr.explore(find=goal)
stdin = simgr.found[0].posix.dumps(0)
print("solve is {}".format(stdin))
print(simgr.found[0].posix.dumps(1))
