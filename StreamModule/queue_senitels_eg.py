import asyncio


async def worker(name, queue):
    while True:
        item = await queue.get()

        try:
            if item is None:
                print(f"{name} stopping")
                return

            print(f"{name} processing {item}")
            await asyncio.sleep(1)
        finally:
            queue.task_done()


async def main():
    queue = asyncio.Queue()
    worker_count = 3

    workers = [
        asyncio.create_task(worker(f"worker-{i}", queue))
        for i in range(worker_count)
    ]

    for item in range(6):
        await queue.put(item)

    # One stop signal for each worker.
    for _ in range(worker_count):
        await queue.put(None)

    await queue.join()
    await asyncio.gather(*workers)


asyncio.run(main())