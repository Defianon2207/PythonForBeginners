import asyncio

async def handle_client(reader, writer):
    try:
        # First 4 bytes represent the message size.
        header = await reader.readexactly(4)
        message_length = int.from_bytes(
            header,
            byteorder="big",
        )

        message_data = await reader.readexactly(
            message_length
        )

        message = message_data.decode()
        print("Received:", message)

        writer.write(b"OK")
        await writer.drain()

    except asyncio.IncompleteReadError:
        print("Client disconnected before sending full message")

    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        8888,
    )

    async with server:
        await server.serve_forever()

asyncio.run(main())