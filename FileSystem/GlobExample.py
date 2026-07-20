#The python used glob module to find files and directory whose name math a pattern.
import glob
import re

python_files = glob.glob("*.py")

print(python_files)

files = glob.glob("FileSystem/*.py")
file = glob.iglob("*.py")

for f in file:
    print("Iteration",f)

#Example of Escape
# Escape all special characters ('?', '*' and '['). This is useful if you want to match an arbitrary literal string that may have special characters in it

print(glob.escape("s*.py"))

#   glob.Translate
glob_pattern = "*.py"
regex_pattern = glob.translate(glob_pattern)

print(regex_pattern)

matcher = re.compile(regex_pattern)

print(bool(matcher.match("app.py")))
print(bool(matcher.match("notes.txt")))