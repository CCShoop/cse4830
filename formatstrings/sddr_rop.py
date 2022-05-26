from pwn import *
import subprocess

class Find_gadget():
    def __init__(self, filename, reqirement_list, operand):
        self._file = filename
        self._req = reqirement_list
        self._op = operand 

    # gets location for execve?
    def one_gadget(self):
        return[int(i) for i in subprocess.check_output(['one_gadget', '--raw', self._file]).decode().split(' ')]

    def test(self):
        pop_list = self.gadget_search()
        req = self._req
        total = []
        temp = []
        thing = 0

        # iterate through req list
        for j in req:
            # iterate through gadget list
            for i in pop_list:
                # if req in gadget
                if j in i:
                    # if gadget in final list don't add it
                    if i in total:
                        #print(i)
                        pass
                    # if gadget not in final list add it    
                    else:
                        # print(i)
                        total.append(i)
                        for k in total:
                            if j not in k:
                                total.remove(k)

        for k in total:
            test = k.split(' ')
            if test[2] == self._op:
                print(k)
            

    # # gets list of all possible gadgets for the file
    # def get_list(self):
    #     return([int(i) for i in subprocess.Popen(['ROPgadget', '--binary', self._file])])
        
    # clears rdi
    def gadget_search(self):
        #total = list(get_list()).split("\n")
        ps = subprocess.Popen(('ROPgadget','--binary', self._file, "--only", self._op), stdout=subprocess.PIPE)
        output = subprocess.check_output(('grep', str(self._req[0])), stdin=ps.stdout)
        return(list(output.decode("utf-8").split('\n')))




# filename = ('libc.so.6')
# filename2 = ('vuln-3')

# gadget = Find_gadget(filename, 1, 1)
# gadget2 = Find_gadget(filename2, 1, 1)
# print(gadget._file)
# print(gadget._req)
# print(gadget._op)
# print(gadget.one_gadget())
# print(gadget2.pop_rdi())