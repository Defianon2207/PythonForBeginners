import asyncio

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

async def main():
    contents = await asyncio.gather(
        asyncio.to_thread(read_file, "file1.txt"),
        asyncio.to_thread(read_file, "file2.txt"),
        asyncio.to_thread(read_file, "file3.txt"),
    )

    for content in contents:
        print(content)

asyncio.run(main())