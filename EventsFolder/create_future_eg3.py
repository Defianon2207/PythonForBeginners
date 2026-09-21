import asyncio
import contextvars

user = contextvars.ContextVar("user",default="Unknow")

async def show_user():
    print("Original User", user.get())

async def main():
    loop = asyncio.get_running_loop()
    user.set("RockSquare")
    modified_user = contextvars.copy_context()
    modified_user.run(user.set,"A.K.A Rahul")
    default_task = loop.create_task(show_user())
    modified_task = loop.create_task(show_user(),context = modified_user)
    await default_task
    await modified_task


asyncio.run(main())