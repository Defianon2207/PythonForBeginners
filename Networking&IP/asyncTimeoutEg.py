import asyncio

async def fetch_user():
    await asyncio.sleep(1)
    print("User fetched")
    return {"name": "Rahul"}

async def fetch_balance():
    await asyncio.sleep(2)
    print("Balance fetched")
    return 50_000

async def main():
    try:
        async with asyncio.timeout(2.5):
            user = await fetch_user()
            balance = await fetch_balance()

            print(user)
            print(balance)

    except TimeoutError:
        print("The complete operation took too long")

asyncio.run(main())