import asyncio
from contextvars import ContextVar

current_user = ContextVar("current_user")


async def process_request(user):
    current_user.set(user)

    await asyncio.sleep(1)

    print(f"Processing request for {current_user.get()}")


async def main():
    await asyncio.gather(
        process_request("Rahul"),
        process_request("Amit"),
    )

user = ContextVar("user", default="Guest")

print(user.get())  # Guest

token = user.set("Rahul")

print(user.get())  # Rahul
print(token.old_value)
user.reset(token)

print(user.get())  

asyncio.run(main())