import asyncio


async def worker(name, ready_event):
    print(f"{name}: waiting for the application")

    await ready_event.wait()

    print(f"{name}: application is ready, starting work")


async def initialize_application(ready_event):
    print("Loading configuration...")
    await asyncio.sleep(1)

    print("Connecting to database...")
    await asyncio.sleep(1)

    print("Initialization complete")

    ready_event.set()


async def main():
    ready_event = asyncio.Event()

    await asyncio.gather(
        worker("Worker 1", ready_event),
        worker("Worker 2", ready_event),
        worker("Worker 3", ready_event),
        initialize_application(ready_event),
    )


asyncio.run(main())