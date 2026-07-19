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