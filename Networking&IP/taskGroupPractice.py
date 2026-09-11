import asyncio

async def fetch_profile():
    await asyncio.sleep(1)
    return {"name": "Rahul"}

async def fetch_balance():
    await asyncio.sleep(2)
    return 50_000

async def fetch_permissions():
    await asyncio.sleep(1)
    return ["read", "write"]

async def build_dashboard():
    async with asyncio.TaskGroup() as tg:
        profile_task = tg.create_task(fetch_profile())
        balance_task = tg.create_task(fetch_balance())
        permissions_task = tg.create_task(fetch_permissions())

    return {
        "profile": profile_task.result(),
        "balance": balance_task.result(),
        "permissions": permissions_task.result(),
    }

async def main():
    dashboard = await build_dashboard()
    print(dashboard)

asyncio.run(main())