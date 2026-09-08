import asyncio
from contextvars import ContextVar


current_user = ContextVar("current_user", default="Guest")


async def login():
    print("Logging in...")
    await asyncio.sleep(1)

    current_user.set("Rahul")
    print(f"Logged in as {current_user.get()}")


async def open_dashboard():
    print("Opening dashboard...")
    await asyncio.sleep(1)

    print(f"Welcome, {current_user.get()}!")


# with asyncio.Runner() as runner:
#     runner.run(login())
#     runner.run(open_dashboard())

#     with asyncio.Runner() as runner:
#     runner.run(first_task())
#     runner.run(second_task())