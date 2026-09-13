import asyncio
import threading

async def calculate(a, b):
    print("Coroutine thread:", threading.current_thread().name)
    await asyncio.sleep(1)
    return a + b

def worker(loop):
    print("Worker thread:", threading.current_thread().name)

    future = asyncio.run_coroutine_threadsafe(
        calculate(10, 20),
        loop,
    )

    # This blocks the worker thread, not the event-loop thread.
    result = future.result(timeout=2)
    print("Result received by worker:", result)

async def main():
    loop = asyncio.get_running_loop()

    await asyncio.to_thread(worker, loop)

asyncio.run(main())