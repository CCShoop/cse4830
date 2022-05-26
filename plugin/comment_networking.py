'''Functions file for network commenting Binary Ninja plugin by Cael Shoop.'''

import sys
from binaryninja import *


def com_sockets():
    for func in bv.functions:
        for il in chain.from_iterable(func.low_level_il):
            if (il.operation == LowLevelILOperation.LLIL_SYSCALL)
                set_comment_at(il.address, '// {Created Socket}')


def com_binds():
    # code


def com_listens():
    # code


def com_accepts():
    # code


def com_connects():
    # code


def com_sendmsgs():
    # code


def com_recvmsgs():
    # code