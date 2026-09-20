import asyncio
import threading
import time


def worker(loop, finished):
    time.sleep(1)
    loop.call_soon_threadsafe(finished.set)


async def main():
    loop = asyncio.get_running_loop()
    finished = asyncio.Event()

    thread = threading.Thread(
        target=worker,
        args=(loop, finished),
    )
    thread.start()

    print("Waiting for worker...")
    await finished.wait()
    print("Worker notified the event loop")

    thread.join()


asyncio.run(main())