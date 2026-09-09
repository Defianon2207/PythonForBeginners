import asyncio


async def download_file():
    print("Download started")
    await asyncio.sleep(3)
    print("Download completed")
    return "report.pdf"


async def main():
    task = asyncio.create_task(download_file())

    print("Doing some other work...")
    await asyncio.sleep(1)
    print("Other work completed")

    filename = await task
    print("Downloaded:", filename)