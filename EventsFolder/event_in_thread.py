import asyncio
import threading


async def show_loop(input):
    loop = asyncio.get_running_loop()

    print(f"Thread:{input}", threading.current_thread().name)
    print("Loop:", loop)


def thread_function():
    asyncio.run(show_loop("thread"))


asyncio.run(show_loop("async"))

thread = threading.Thread(
    target=thread_function,
    name="WorkerThread",
)

thread.start()
thread.join()