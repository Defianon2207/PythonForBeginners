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

# async def fetch_users():
#     await asyncio.sleep(1)
#     return ["Rahul", "Amit"]


# async def fetch_orders():
#     await asyncio.sleep(1)
#     return [101, 102]


# async def main():
#     users, orders = await asyncio.gather(
#         fetch_users(),
#         fetch_orders(),
#     )

#     print(users)
#     print(orders)
# asyncio.run(main())

# users = asyncio.run(fetch_users())
# orders = asyncio.run(fetch_orders())

# The second version creates and closes two independent event loops. Tasks, connections, futures and context belonging to the first loop cannot simply be reused by the second loop.