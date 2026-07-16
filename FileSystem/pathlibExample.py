from pathlib import Path

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

