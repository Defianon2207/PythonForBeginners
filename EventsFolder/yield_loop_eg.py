import asyncio


async def resource_stream():
    print("Resource opened")

    try:
        for number in range(5):
            await asyncio.sleep(0.5)
            yield number
    finally:
        print("Resource closed")


async def consumer():
    async for number in resource_stream():
        print("Received:", number)

        if number == 1:
            print("Consumer returning early")
            return


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(consumer())
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()