import asyncio


async def main():
    proc = await asyncio.create_subprocess_exec(
        "python3",
        "-u",
        "-c",
        (
            "import time\n"
            "for i in range(5):\n"
            "    print(f'Progress: {i}', flush=True)\n"
            "    time.sleep(1)\n"
        ),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    async for line in proc.stdout:
        print("SUBPROCESS:", line.decode().rstrip())

    await proc.wait()

    print("Exit code:", proc.returncode)


asyncio.run(main())