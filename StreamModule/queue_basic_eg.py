import asyncio


async def producer(queue):
    for item in ["BTC", "ETH", "SOL"]:
        print(f"Producing {item}")
        await queue.put(item)
        await asyncio.sleep(0.5)

    # Special value telling the consumer to stop.
    await queue.put(None)


async def consumer(queue):
    while True:
        item = await queue.get()

        try:
            if item is None:
                print("Consumer stopping")
                return

            print(f"Processing {item}")
            await asyncio.sleep(1)
            print(f"Finished {item}")

        finally:
            queue.task_done()


async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task

    # Wait until every queued item is marked completed.
    await queue.join()

    await consumer_task


asyncio.run(main())


#OTHER METHODS

#queue = asyncio.Queue(maxsize=0)
#Queue.qsize()
#queue.empty()
#queue.full()
#queue.no_wait()
#task_done()
#queue.join()