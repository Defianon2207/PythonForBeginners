import asyncio


def announce(message):
    print(message)


async def main():
    loop = asyncio.get_running_loop()

    print("Timer scheduled")
    loop.call_later(2, announce, "About two seconds passed")

    await asyncio.sleep(2.5)
    print("main() finished")


asyncio.run(main())