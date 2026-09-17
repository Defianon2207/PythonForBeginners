import asyncio
import time

async def run(name,delay):
    proc = await asyncio.create_subprocess_exec(
        "python3",
        "-c",
        (
            "import time; "
            f"time.sleep({delay}); "
            f"print({name!r})"
        ),
        stdout=asyncio.subprocess.PIPE,
    )

    stdout , _ = await proc.communicate()
    print(stdout.decode().strip())

async def main():
    started = time.perf_counter()

    await asyncio.gather(
        run("Task A", 2),
        run("Task B", 2),
        run("Task C", 2),
    )

    duration = time.perf_counter() - started
    print(f"Completed in {duration:.2f} seconds")


asyncio.run(main())