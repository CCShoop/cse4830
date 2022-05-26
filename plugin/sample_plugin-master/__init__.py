from binaryninja import *
import comment_networking.py


PluginCommand.register_for_address("Comment Sockets", "Adds comments to socket syscalls", com_sockets)
PluginCommand.register_for_address("Comment Binds", "Adds comments to bind syscalls", com_binds)
PluginCommand.register_for_address("Comment Listens", "Adds comments to listen syscalls", com_listens)
PluginCommand.register_for_address("Comment Accepts", "Adds comments to accept syscalls", com_accepts)
PluginCommand.register_for_address("Comment Connects", "Adds comments to connect syscalls", com_connects)
PluginCommand.register_for_address("Comment Send/Sendmsgs", "Adds comments to send/sendmsg syscalls", com_sendmsgs)
PluginCommand.register_for_address("Comment Recvmsgs", "Adds comments to recv/recvmsg syscalls", com_recvmsgs)
