import asyncio

async def main():
    reader, writer = await asyncio.open_connection(
        "127.0.0.1",
        8888,
    )

    try:
        messages = ["Hello", "How are you?", "Goodbye"]

        for message in messages:
            writer.write(f"{message}\n".encode())
            await writer.drain()

            response = await reader.readline()
            print("Received:", response.decode().rstrip())

    finally:
        writer.close()
        await writer.wait_closed()

asyncio.run(main())