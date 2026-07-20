import tempfile
import os 
from pathlib import Path

with tempfile.TemporaryFile() as file:
    file.write(b"Hello, Rahul!")

    file.seek(0)
    content = file.read()

    print(content)

    # To work with ordinary string use 'w+'

with tempfile.TemporaryFile(mode="w+", encoding="utf-8") as file:
    file.write("Temporary text data")

    file.seek(0)
    print(file.read())

with tempfile.TemporaryFile(
    mode="w+",
    encoding="utf-8"
) as file:
    file.write("नमस्ते")

    file.seek(0)
    print(file.read())

    with tempfile.TemporaryFile(
    mode="w+",
    encoding="utf-8"
    ) as file:

    # Write emojis and text
        file.write("Hello Rahul! 😊\n")
        file.write("Python is fun 🐍🔥\n")
        file.write("Have a great day 🚀🎉")

    # Move the pointer back to the beginning
        file.seek(0)

    # Read the temporary file
        content = file.read()
        print(content)


#NamedTemporaryFile
with tempfile.NamedTemporaryFile(
    mode="w+",
    encoding="utf-8",
    suffix=".txt",
    prefix="emoji_"
) as file:
    file.write("Hello Rahul 😊\n")
    file.write("Learning Python 🐍🚀")
    file.flush()

    print("File path:", file.name)
    print("Exists inside block:", os.path.exists(file.name))

    file.seek(0)
    print(file.read())

print("Exists after block:", os.path.exists(file.name))


#Opening file with Name

with tempfile.NamedTemporaryFile(
    mode="w+",
    encoding="utf-8",
    suffix=".txt",
    delete=True,
    delete_on_close=False
) as temp:
    temp.write("Python 🐍\nTemporary file 📄")
    temp.flush()

    path = temp.name
    print("Temporary path:", path)

    # Open the same file separately using its visible path
    with open(path, mode="r", encoding="utf-8") as reader:
        print(reader.read())

#SpooledTemporaryFile 
# If data moves beyond specified size it is moved to memory

with tempfile.SpooledTemporaryFile(
    max_size =20,
    mode = "w+",
    encoding = "utf-8"   
) as file:
    file.write("Hello Rahul 😊")
    print("Rolled to disk:", file._rolled)

    file.write("—but now the content is much larger 😊")
    print("Rolled to disk:", file._rolled)

    file.seek(0)
    print(file.read())


#tempfile.TemporaryDirectory()  securely creates a temporay Directory an deletes it after the files is closed
with tempfile.TemporaryDirectory() as temp_dir:
    print("Temporary directory:", temp_dir)
    print("Exists inside block:", os.path.exists(temp_dir))

print("Exists after block:", os.path.exists(temp_dir))


#Creating file in temp Directory

with tempfile.TemporaryDirectory() as temp_dir:
    directory = Path(temp_dir)

    notes_file = directory / "notes.txt"
    notes_file.write_text(
        "Learning Python 🐍🚀",
        encoding="utf-8"
    )

    print(notes_file.read_text(encoding="utf-8"))
    print("Files:", list(directory.iterdir()))


    #Explicit cleanup with cleanup

temp = tempfile.TemporaryDirectory()

print("Path:", temp.name)
print("Before cleanup:", os.path.exists(temp.name))

temp.cleanup()

print("After cleanup:", os.path.exists(temp.name))

#tempfile.mkstemp() securely creates a temporary file and returns two things:

fd, path = tempfile.mkstemp()

print("File descriptor:", fd)
print("File path:", path)

os.close(fd)
os.remove(path)

#Writing and reading the binary

fd, path = tempfile.mkstemp()

try:
    os.write(fd, b"Hello from a temporary file")

    # Move the OS-level file position back to the beginning
    os.lseek(fd, 0, os.SEEK_SET)

    content = os.read(fd, 100)
    print(content)

finally:
    os.close(fd)
    os.remove(path)

#MKdtemp

temp_dir = tempfile.mkdtemp()

print("Directory:", temp_dir)
print("Exists:", os.path.exists(temp_dir))
print("Absolute path:", os.path.isabs(temp_dir))
os.rmdir(temp_dir)

#tempfile.gettempprefix()
#tempfile.gettempprefixb()
#tempfile.gettempdir()
#tempfile.gettempdirb()
