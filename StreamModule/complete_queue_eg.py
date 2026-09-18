import asyncio
import random


async def producer(queue):
    for job_id in range(1, 11):
        job = {
            "id": job_id,
            "duration": random.uniform(0.5, 1.5),
        }

        print(f"Created job {job_id}")
        await queue.put(job)

    queue.shutdown()
    print("Producer shut down the queue")


async def worker(name, queue):
    while True:
        try:
            job = await queue.get()
        except asyncio.QueueShutDown:
            print(f"{name} stopping")
            return

        try:
            print(f"{name} processing job {job['id']}")

            await asyncio.sleep(job["duration"])

            print(f"{name} completed job {job['id']}")
        finally:
            queue.task_done()


async def main():
    queue = asyncio.Queue(maxsize=3)

    workers = [
        asyncio.create_task(worker(f"worker-{i}", queue))
        for i in range(1, 4)
    ]

    await producer(queue)

    # Wait for every accepted job to finish.
    await queue.join()

    # Wait for workers to observe QueueShutDown and exit.
    await asyncio.gather(*workers)

    print("All jobs completed")


asyncio.run(main())