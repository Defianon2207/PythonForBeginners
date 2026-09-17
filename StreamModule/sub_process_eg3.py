#Sending input with communicate

import asyncio


async def main():
    proc = await asyncio.create_subprocess_exec(
        "python3",
        "-c",
        "import sys; print(sys.stdin.read().upper())",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate(
        input=b"hello from Rahul"
    )

    print("Output:", stdout.decode().strip())
    print("Exit code:", proc.returncode)


asyncio.run(main())