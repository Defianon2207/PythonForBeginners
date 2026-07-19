import os
import stat
import socket
info = os.stat('pathlibExample.py')
#ISREG is used to check of the file is of regular mode or not.
print(info, stat.S_ISREG(info.st_mode))

#ISDIR is used to check if the give file is directory 

print(stat.S_ISDIR(info.st_mode)) #This retursn false as this is a regular file

#ISCHR checks whether a path i s chr_device

info = os.stat("/dev/null")

print("ISCHR",stat.S_ISCHR(info.st_mode))

#FIFO
fifo_path = "message_pipe"
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

info = os.stat(fifo_path)
print("FIFO",stat.S_ISFIFO(info.st_mode))


#IS_SOCK

socket_path = "application.sock"

if os.path.exists(socket_path):
    os.remove(socket_path)

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(socket_path)

info = os.stat(socket_path)

print("Is socket:", stat.S_ISSOCK(info.st_mode))

server.close()
os.remove(socket_path)

#IS_WHT
path = "/path/to/whiteout"

if hasattr(stat, "S_ISWHT") and os.path.lexists(path):
    mode = os.lstat(path).st_mode
    print("Is whiteout:", stat.S_ISWHT(mode))
else:
    print("Whiteouts are unsupported or the path does not exist")


#S_IMODE

info = os.stat("StatExample.py")
permissions = stat.S_IMODE(info.st_mode)

print(permissions)
print(oct(permissions))
print(stat.filemode(info.st_mode))