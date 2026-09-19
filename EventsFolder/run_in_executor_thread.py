import asyncio
import time


def save_large_file():
    print("Saving started")
    time.sleep(3)
    print("Saving finished")


async def main():
    loop = asyncio.get_running_loop()

    # Submit the function, but don't await its result.
    loop.run_in_executor(None, save_large_file)

    print("main() finished")


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    print("Waiting for executor threads...")

    loop.run_until_complete(
        loop.shutdown_default_executor()
    )

    print("Executor shut down")
    loop.close()


    # Use shutdown with timeout
    # loop.shutdown_default_executor(timeout=5) 