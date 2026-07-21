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

result = shutil.copy("first.txt","folder_a")
print(result)

# shutil.copy2(src, dst, *, follow_symlinks=True)
# Identical to copy() except that copy2() also attempts to preserve file metadata.

#shutil.ignore_patterns
# This factory function creates a function that can be used as a callable for copytree()'s ignore argument, ignoring files and directories that match one of the glob-style patterns provided. See the example below.
# Example 
# shutil.ignore_patterns(
#         "*.log",
#         "*.pyc",
#         "__pycache__"
#     )


# Copy Tree example 

#Commenting this so no new folders are created 
# result = shutil.copytree("folder_a", "FileSysytem_backup")
# shutil.rmtree("FileSysytem_backup")

# shutil.move(src, dst, copy_function=copy2)

usage = shutil.disk_usage("folder_a")
print("Usage -> ", usage)

# shutil.chown(path, user=None, group=None, *, dir_fd=None, follow_symlinks=True)
# Change owner user and/or group of the given path.

python_path = shutil.which("python3")

print(python_path)

ffmpeg = shutil.which("ffmpeg")
print(ffmpeg)

#By default, which() searches directories listed in the system’s PATH environment variable.

#You can provide custom path to it 
# result = shutil.which(
#     "python3",
#     path="/usr/bin:/opt/homebrew/bin"
# )


#Archival operations
# shutil.make_archive("backup", "zip", root_dir="folder_a")

print(shutil.get_archive_formats())
print(shutil.get_unpack_formats())

# shutil.register_archive_format
# shutil.unregister_archive_format(name)
# shutil.unpack_archive(filename[, extract_dir[, format[, filter]]])

# shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])
# shutil.unregister_unpack_format(name)

