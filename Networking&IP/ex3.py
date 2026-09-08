import asyncio
from contextvars import ContextVar


current_user = ContextVar("current_user", default="Guest")


async def login_user():
    print("Logging in...")
    await asyncio.sleep(1)

    current_user.set("Rahul")
    print("Logged in as:", current_user.get())


async def show_dashboard():
    await asyncio.sleep(1)
    print(f"Welcome to your dashboard, {current_user.get()}!")


with asyncio.Runner() as runner:
    runner.run(login_user())
    runner.run(show_dashboard())