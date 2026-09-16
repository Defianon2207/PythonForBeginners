import asyncio


async def worker(event):
    print("Waiting for round 1")
    await event.wait()
    print("Running round 1")

    event.clear()

    print("Waiting for round 2")
    await event.wait()
    print("Running round 2")


async def controller(event):
    await asyncio.sleep(1)
    print("Start round 1")
    event.set()

    await asyncio.sleep(1)
    print("Start round 2")
    event.set()


async def main():
    event = asyncio.Event()

    await asyncio.gather(
        worker(event),
        controller(event),
    )


asyncio.run(main())