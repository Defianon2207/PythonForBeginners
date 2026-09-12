import asyncio

async def fetch_data():
    try:
        print("Fetching data...")
        await asyncio.sleep(5)
        return "Data received"

    except asyncio.CancelledError:
        print("fetch_data was cancelled")
        raise

async def main():
    try:
        result = await asyncio.wait_for(
            fetch_data(),
            timeout=2,
        )

        print(result)

    except TimeoutError:
        print("Fetching exceeded two seconds")

asyncio.run(main())