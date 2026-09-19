import asyncio
import time
import threading


def blocking_work():
    print("Worker thread:", threading.current_thread().name)
    time.sleep(2)
    print("Blocking work completed")
    return 100


async def main():
    loop = asyncio.get_running_loop()

    result = await loop.run_in_executor(
        None,
        blocking_work,
    )

    print("Result:", result)


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.run_until_complete(
        loop.shutdown_default_executor()
    )
    loop.close()