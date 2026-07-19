import os

print(os.getcwd())
print(os.path.abspath("FileSystem.txt"))

paths = [
    "/Users/rahul/project/src/main.py",
    "/Users/rahul/project/src/utils.py",
    "/Users/rahul/project/tests/test.py"
]

print(os.path.commonpath(paths))

# Example of common path
paths = [
    "apple.txt",
    "application.py",
    "apply.doc"
]

print(os.path.commonprefix(paths))

# Example of dirname 
path = "/home/rahul/Documents/report.pdf"

print(os.path.dirname(path))

#lexists() if you ask about danggling symlink it will return true
#Expand user tilde is shorthand for current user directory 

print(os.path.expanduser("~/Documents"))


#Example of exapandvars
path = "$HOME/Documents"

print(os.path.expandvars(path))

#Example of a getatime()

timestamp = os.path.getatime("OsPathExample.py")

print(timestamp)

#Read about getmtime and getctime

#getSize of the file in bytes
print(os.path.getsize('OsPathExample.py'))

#Read about islink, isjunction, ismount, isfile,isdir, path.join

#isReserved is not a function of posixPath
# print(os.path.isreserved("report.txt"))

#example of relpath

path = "project/images/logo.png"
start = "project/src"

print(os.path.relpath(path, start))

#example of splitdrive
import os

print(os.path.splitroot("/home/rahul/report.txt"))