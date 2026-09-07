import asyncio


async def download(name,seconds):
    print(f"starting, {name}")
    await asyncio.sleep(seconds)
    print(f"Completed {name}")

async def main():
    await asyncio.gather(
        download("File A", 1),
        download("File B", 1)
    )

asyncio.run(main())