import asyncio

async def process_data():
    print("Processing started")
    await asyncio.sleep(4)
    print("Processing completed")

async def main():
    timeout_manager = None

    try:
        async with asyncio.timeout(None) as timeout_manager:
            print("No deadline currently configured")

            loop = asyncio.get_running_loop()

            # Set the deadline to 2 seconds from now.
            deadline = loop.time() + 2
            timeout_manager.reschedule(deadline)

            await process_data()

    except TimeoutError:
        print("Processing timed out")

    if timeout_manager.expired():
        print("The deadline was exceeded")

asyncio.run(main())