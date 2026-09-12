import asyncio

async def fetch_database():
    await asyncio.sleep(3)
    return "database result"

async def main():
    try:
        # Entire operation must finish within 5 seconds.
        async with asyncio.timeout(5):

            try:
                # Database call gets only 1 second.
                async with asyncio.timeout(1):
                    result = await fetch_database()
                    print(result)

            except TimeoutError:
                print("Database request timed out")

            print("Continuing with fallback data")

    except TimeoutError:
        print("The entire operation timed out")

asyncio.run(main())