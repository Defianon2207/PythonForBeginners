import asyncio
import threading


async def show_loop():
    loop = asyncio.get_running_loop()

    print("Thread:", threading.current_thread().name)
    print("Loop:", loop)


def thread_function():
    asyncio.run(show_loop())


asyncio.run(show_loop())

thread = threading.Thread(
    target=thread_function,
    name="WorkerThread",
)

thread.start()
thread.join()