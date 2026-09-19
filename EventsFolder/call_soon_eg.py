import asyncio


def greet(name):
    print(f"Hello, {name}")


async def main():
    loop = asyncio.get_running_loop()

    print("Before scheduling")
    loop.call_soon(greet, "Rahul")
    print("After scheduling")

    await asyncio.sleep(0)
    print("After yielding to the loop")


asyncio.run(main())