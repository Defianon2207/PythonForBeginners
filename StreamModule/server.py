import asyncio

async def handle_client(reader, writer):
    address = writer.get_extra_info("peername")

    try:
        while True:
            data = await reader.readline()

            if not data:
                break

            message = data.decode().rstrip("\n")
            print(f"{address}: {message}")

            writer.write(data)
            await writer.drain()

    finally:
        writer.close()
        await writer.wait_closed()
        print(f"Disconnected: {address}")

async def main():
    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        8888,
    )

    async with server:
        await server.serve_forever()

asyncio.run(main())