import asyncio

async def producer(future):
    print("Preparing result...")
    await asyncio.sleep(2)

    future.set_result("Payment completed")

async def consumer(future):
    print("Waiting for result...")

    result = await future

    print("Received:", result)

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    producer_task = asyncio.create_task(producer(future))
    consumer_task = asyncio.create_task(consumer(future))

    await producer_task
    await consumer_task

asyncio.run(main())