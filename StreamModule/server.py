import asyncio

async def handle_client(reader, writer):
    # Information about the connected client
    address = writer.get_extra_info("peername")
    print(f"Client connected: {address}")

    # Wait for up to 100 bytes
    data = await reader.read(100)

    message = data.decode()
    print(f"Received: {message!r}")

    # Send the same data back
    print(f"Sending back: {message!r}")
    writer.write(data)
    await writer.drain()

    # Close this client's connection
    print(f"Closing connection: {address}")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        8888,
    )

    addresses = ", ".join(
        str(socket.getsockname())
        for socket in server.sockets
    )
    print(f"Server running on {addresses}")

    async with server:
        await server.serve_forever()

asyncio.run(main())