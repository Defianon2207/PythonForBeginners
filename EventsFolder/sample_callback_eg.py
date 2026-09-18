import asyncio


def callback():
    loop = asyncio.get_running_loop()
    print("Callback's loop:", loop)


async def main():
    loop = asyncio.get_running_loop()

    loop.call_soon(callback)

    await asyncio.sleep(0.1)
    running_loop = asyncio.get_running_loop()
    event_loop = asyncio.get_event_loop()

    print("Check running loop is event loop",running_loop is event_loop)


asyncio.run(main())