import fnmatch
import os

result = fnmatch.fnmatch("notes.txt", "*.txt")

print(result)

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "*.txt"):
        print(file)

print(fnmatch.fnmatch("first.txt", "firs?.txt"))
print(fnmatch.fnmatch("first.txt", "firs[q-z].txt"))

#matchcase
print(fnmatch.fnmatchcase("REPORT.TXT", "*.txt"))
print(fnmatch.fnmatchcase("report.txt", "*.txt"))

#Filter, FilterFalse and Translate

files = [
    "app.py",
    "test.py",
    "notes.txt",
    "report.txt",
    "image.png",
]

text_files = fnmatch.filter(files, "*.txt")

print(text_files)

pattern = "*.txt"
regex_pattern = fnmatch.translate(pattern)

print(regex_pattern)

#use this with re module will learn in future