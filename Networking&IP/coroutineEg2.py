import asyncio
import random

# Producer Coroutine: Generates work items and puts them into the queue
async def producer(queue: asyncio.Queue, count: int):
    for i in range(1, count + 1):
        item = f"Job-{i}"
        await queue.put(item)
        print(f"[Producer] Added {item} to queue.")
        await asyncio.sleep(0.2)  # Simulate time spent generating jobs
        
    print("[Producer] Finished adding all jobs.")

# Consumer Coroutine: Pulls work items from the queue and processes them
async def consumer(worker_id: int, queue: asyncio.Queue):
    while True:
        # Retrieve an item from the queue (suspends until an item is available)
        item = await queue.get()
        
        print(f"  [Worker {worker_id}] Started processing {item}")
        processing_time = random.uniform(0.5, 1.5)
        await asyncio.sleep(processing_time)  # Simulate I/O bound processing task
        print(f"  [Worker {worker_id}] Finished {item} in {processing_time:.2f}s")
        
        # Notify the queue that the retrieved item has been processed
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=5)

    # Start 3 consumer workers in the background
    workers = [
        asyncio.create_task(consumer(worker_id=i, queue=queue))
        for i in range(1, 4)
    ]

    # Run the producer to populate the queue
    await producer(queue, count=6)

    # Block until all items in the queue have been fully processed
    await queue.join()

    # Cancel background worker tasks since queue is empty
    for worker in workers:
        worker.cancel()

if __name__ == "__main__":
    asyncio.run(main())