from pathlib import Path, PurePath

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
# PathLib.PurePosicPath()