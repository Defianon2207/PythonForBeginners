import asyncio

async def download_file():
    try:
        for progress in range(1, 11):
            print(f"Downloading: {progress * 10}%")
            await asyncio.sleep(1)

        return "Download completed"

    except asyncio.CancelledError:
        print("Download was cancelled")

        # Perform cleanup here if required
        print("Removing temporary file...")

        # Re-raise the exception to confirm cancellation
        raise

async def main():
    task = asyncio.create_task(download_file())

    # Let the task run for three seconds
    await asyncio.sleep(3)

    print("Requesting cancellation...")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Main confirmed that the task was cancelled")

asyncio.run(main())