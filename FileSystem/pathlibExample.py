from pathlib import Path, PurePath, PurePosixPath
import os

p = Path("..")
print(p)

for x in p.iterdir() :
    print("p Print",x,x.is_file())

print(list(p.glob('**/*.py')))

z = Path('/etc')
q = z/'init.d'/'reboot'
print(q.resolve())
print(q.exists())
print(q.is_dir())

# Print files which are listed in the 

for x in p.iterdir():
    if x.is_file():
        print(f"\nFileName : {x}")
    elif x.is_dir():
        print(f"\nDirectory : {x}")
        for y in x.iterdir():
            print(f"Files in Directory {x}: {y}")


# Open a file and print the content line by line

# for x in p.iterdir():
#     if x.is_file():
#         with x.open() as f:
#             print(f.readline())


#Examples of pure path object

print(PurePath('pathlibExample.py'))
p = PurePath('pathlibExample.py')
print(p.__repr__(), p.__str__(), p.parent)

k = PurePath('.')
print(k.__str__(), k.parts)

q = PurePath("/c","/usr", "/etc", "lib64")
print(q)

# If inputs are relative

m = PurePath('Desktop','SecondaryProject','Extrnl')
print(m)

#Example 3

z = PurePath('File','/Desktop','/usr','/etc','log')
print(z)

# You can create PurePosixPath without even touching the file system
# PathLib.PurePosicPath() similary PathLib.PureWindowsPath

files = {
      PurePosixPath("main.py"): "Python file",
        PurePosixPath("README.md"): "Documentation"
}

print(files[PurePosixPath("main.py")])

#Paths of same flavor are comparable

print(
    PurePosixPath("extrnl") ==
    PurePosixPath("extrnl")
)

print(
    PurePosixPath("extrnl") ==
    PurePosixPath("extrnlD")
)

# Paths are case sensitive

print(
     PurePosixPath("extrnl") ==
     PurePosixPath("extrnL")
)

# / example for creating path

new_path = PurePath('/etc')
new_path2 = new_path/PurePath('bin')

print(new_path2, type(new_path2))

#If path is absolute it only accept the things on righ to left

new_path3 = PurePath('/bin')/new_path
print(new_path3)

#paths can be easily converted to string

str_eg = PurePath('/etc')
convert_to_string = str(str_eg)

#Check the type both are different, similarly it can be converted into 
print(type(str_eg),type(convert_to_string))

p = PurePosixPath("/etc")

print(bytes(p))
print(os.fsencode(p))

#Accessing different parts
p = PurePath('/usr/bin/python3')
print(p.parts)