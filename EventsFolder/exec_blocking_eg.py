import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def blocking_job(number):
    time.sleep(2)
    return number * 2


async def main():
    loop = asyncio.get_running_loop()

    work_executor = ThreadPoolExecutor(max_workers=20)

    try:
        jobs = [
            loop.run_in_executor(
                work_executor,
                blocking_job,
                number,
            )
            for number in range(50)
        ]

        # DNS continues using asyncio's default executor.
        addresses = await loop.getaddrinfo(
            "example.com",
            443,
            type=socket.SOCK_STREAM,
        )

        print("Resolved:", addresses[0][4])

        await asyncio.gather(*jobs)

    finally:
        work_executor.shutdown()


asyncio.run(main())