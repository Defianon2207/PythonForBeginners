import asyncio


async def download_file():
    print("Downloading file...")
    await asyncio.sleep(3)
    print("File downloaded")


async def fetch_user():
    print("Fetching user...")
    await asyncio.sleep(2)
    print("User fetched")


async def main():
    await asyncio.gather(
        download_file(),
        fetch_user()
    )


asyncio.run(main())