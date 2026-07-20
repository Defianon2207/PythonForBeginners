import os
import stat
import socket
import pwd
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

#S_IFMT
mode = os.stat("StatExample.py").st_mode

file_type = stat.S_IFMT(mode)

print("Complete mode:", oct(mode))
print("File type:", oct(file_type))
print("Permissions:", oct(stat.S_IMODE(mode)))

#filemode
info = os.stat("StatExample.py")

print("Numeric mode:", oct(info.st_mode))
print("Readable mode:", stat.filemode(info.st_mode))

# stat.ST_INO An inode is the filesystem’s internal record for a file. The inode number identifies that record within a particular filesystem

info = os.stat("StatExample.py")

inode = info[stat.ST_INO]

print("Inode number:", inode)
#ST_DEV
device = info[stat.ST_DEV]

print("Device number:", device)

#stat.ST_NLINK — number of hard links This tells you how many directory entries (filenames) point to the same inode.

#stat.ST_UID — user ID of the owner Every Unix user has a numeric user ID called a UID. ST_UID tells you which user owns the file.
uid = info[stat.ST_UID]

print("Owner UID:", uid)
print("Using attribute:", info.st_uid)
owner = pwd.getpwuid(info.st_uid).pw_name

print("Owner UID:", info.st_uid)
print("Owner name:", owner)

#GID

gid = info[stat.ST_GID]

print("Owner group ID:", gid)
print("Using attribute:", info.st_gid)

# *** Read ONly ***
# stat.ST_SIZE
# Size in bytes of a plain file; amount of data waiting on some special files.

# stat.ST_ATIME
# Time of last access.

# stat.ST_MTIME
# Time of last modification

# Example of S_IFSOCK

path = "server.sock"

if os.path.exists(path):
    os.remove(path)

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(path)

mode = os.stat(path).st_mode

print(stat.S_IFMT(mode) == stat.S_IFSOCK)
print(stat.S_ISSOCK(mode))
print(stat.filemode(mode))

server.close()
os.remove(path)

#Sticky Bit Directory

mode = os.stat("/tmp").st_mode

print("Permissions:", stat.filemode(mode))
print("Sticky bit set:", bool(mode & stat.S_ISVTX))

# These are bitmask constants used to check or modify the file owner’s permissions.

# stat.S_IRWXU: all owner permissions—read, write and execute.
# stat.S_IRUSR: owner read permission.
# stat.S_IWUSR: owner write permission.


# path = "example.txt"

# with open(path, "w") as file:
#     file.write("Hello")

# # Owner: read and write
# # Group: read
# # Others: no permissions
# os.chmod(path, 0o640)

# mode = os.stat(path).st_mode

# print("Permissions:", stat.filemode(mode))

# print("Owner permission bits:", oct(mode & stat.S_IRWXU))
# print("Owner can read:", bool(mode & stat.S_IRUSR))
# print("Owner can write:", bool(mode & stat.S_IWUSR))

# owner_permissions = mode & stat.S_IRWXU

# print(oct(owner_permissions))


#Things to remember
 
# IR - Read right
# IW - Write right
# IX - Execute right

# USR - Users
# GRP - Group
# OTH- Others


# Example permissions = stat.S_IRUSR | stat.S_IWUSR

# os.chmod("example.txt", permissions)

# mode = os.stat("example.txt").st_mode
# print(stat.filemode(mode))

info = os.stat("StatExample.py")
user_flags = info.st_flags & stat.UF_SETTABLE
print("All flags:", info.st_flags)
print("User-settable flags currently enabled:", user_flags)