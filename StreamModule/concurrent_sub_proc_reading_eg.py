import asyncio


async def read_stream(label, stream):
    async for line in stream:
        print(f"[{label}] {line.decode().rstrip()}")


async def main():
    proc = await asyncio.create_subprocess_exec(
        "python3",
        "-u",
        "-c",
        (
            "import sys, time\n"
            "for i in range(3):\n"
            "    print(f'normal {i}', flush=True)\n"
            "    print(f'error {i}', file=sys.stderr, flush=True)\n"
            "    time.sleep(1)\n"
        ),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    await asyncio.gather(
        read_stream("stdout", proc.stdout),
        read_stream("stderr", proc.stderr),
    )

    await proc.wait()
    print("Exit code:", proc.returncode)


asyncio.run(main())