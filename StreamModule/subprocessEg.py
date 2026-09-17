import asyncio


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()

    print(f"[{cmd!r} exited with {proc.returncode}]")

    if stdout:
        print(f"[stdout]\n{stdout.decode()}")

    if stderr:
        print(f"[stderr]\n{stderr.decode()}")

    command = 'sleep 1; echo "Hello from shell"'

    proc = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()

    print(stdout.decode().strip())
    print("Exit code:", proc.returncode)


asyncio.run(run("ls"))