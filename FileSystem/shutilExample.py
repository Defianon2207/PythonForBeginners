import shutil
import tempfile
import stat
import os
import time

with open("first.txt","rb") as source:
    with open("second.txt","wb") as destination:
        shutil.copyfileobj(source,destination)


#Example of flush close and seek

with tempfile.TemporaryFile(mode="w+b") as destination:
    source = open("first.txt", "rb")

    shutil.copyfileobj(source, destination)

    destination.flush()  # Push buffered data to the file
    destination.seek(0)  # Move cursor back to the beginning

    print(destination.read())

    source.close()


#Example of copyfile
source = "first.txt"
destination ="third.txt"
shutil.copyfile(source, destination)

#Example of copyMode
shutil.copymode(source, destination)
source_mode = stat.filemode(os.stat(source).st_mode)
destination_mode = stat.filemode(os.stat(destination).st_mode)

print(source_mode)
print(destination_mode)


#shutil.copystat() copies a file’s metadata from the source to the destination without copying its contents.
# It copies :
# Permission bit
# Last access time 
# Last Modification Time 
# File Flags

# It does not copy
# File content
# Owner
# Group

os.chmod(source, 0o755)
os.chmod(destination, 0o600)
# Give the source an older access and modification time
old_time = time.time() - 86400  # 24 hours ago
os.utime(source, (old_time, old_time))

# Copy the source's metadata to the destination
shutil.copystat(source, destination)

source_info = os.stat(source)
destination_info = os.stat(destination)

print("Source permissions:")
print(stat.filemode(source_info.st_mode))

print("Destination permissions:")
print(stat.filemode(destination_info.st_mode))

print("Source modification time:")
print(time.ctime(source_info.st_mtime))

print("Destination modification time:")
print(time.ctime(destination_info.st_mtime))


#Example of shutil.copy
