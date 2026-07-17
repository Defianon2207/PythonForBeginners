from pathlib import Path, PurePath, PurePosixPath, PureWindowsPath
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

print(PurePosixPath("/etc").parser)
print(PureWindowsPath("C:/Windows").parser)

#POSIX Relative PATH
p = PurePosixPath("etc/nginx")

print("Drive :", p.drive)
print("Root  :", p.root)
print("Anchor:", p.anchor)


#Example of parent and parents 


p = PurePosixPath("/home/rahul/projects/ai")
print(p.parent)

#Resolve
p = Path("foo/..")

print("Resolve",p.resolve())


#PurePath.name¶
#A string representing the final path component, excluding the drive and root, if any:
p = PurePosixPath("/home/rahul/projects/ai.txt")
print(p.suffix, p.stem) # It also has suffixes

#Absolut path
print(PurePosixPath('/a/b').is_absolute())
print(PurePosixPath('a/b').is_absolute())

#Relative to
p = PurePath('/etc/passwd')
print(p.is_relative_to('/etc'))

#Is_reserved used in windows

#Join Path

print(PurePosixPath('/etc').joinpath('passwd'))

#Full_match
print(PurePath('a/b.py').full_match('a/*.py'))
print(PurePath('a/b.py').full_match('*.py'))

#Match
print(PurePath('a/b.py').match('*.py'))

#Read about with_name, with_stem, with_suffix

#Moving to concrete path

#Python reading the 

p = Path("../Notes/FileSystem.txt")
print("Does Path exists: ","Yes, it exists." if p.exists() else "No, this file doesn't exist.")
with p.open('r') as file:
    for line in file:
        print(line, end="")


#Python URI

uri = Path.from_uri('file:///Users/rahulsingh/Desktop/Python-Streams/DDoS/FileSystem')
print(uri)
print(type(uri))

#Example of .home

home = Path.home()
print(home)

#Example of expanduser

p = Path("~/Desktop")
print(p.expanduser())
print(Path.cwd())

# Absolute example

p = Path("FileSystem.txt")
print("Absolute Path : ",p.absolute())

#Example of Resolve

p = Path()
print("Resolved Path",p.resolve())

#Example of SymLink

# link = Path("myLink") #Delete the myLink file when you want to rerun this file
# link.symlink_to("../Notes/FileSystem.txt")

# print(link.readlink())

#Example of stat

p = Path("../Notes/FileSystem.txt")
print(p.stat().st_size, "bytes", p.stat().st_mode)
# print(list[p.stat()])
#is_socket()
#is_mount()
#is_dir()
#is_file()
#is_stat()
#is_lstat()
#exists()
#is_symlink()





