import asyncio


async def fetch_user():
    print("Fetching user...")
    await asyncio.sleep(1)
    return {"id": 1, "name": "Rahul"}


async def fetch_orders(user_id):
    print(f"Fetching orders for user {user_id}...")
    await asyncio.sleep(1)
    return ["Laptop", "Keyboard", "Monitor"]


with asyncio.Runner() as runner:
    user = runner.run(fetch_user())
    orders = runner.run(fetch_orders(user["id"]))

    print("User:", user)
    print("Orders:", orders)