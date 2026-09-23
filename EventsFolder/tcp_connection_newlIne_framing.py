import asyncio


class LineProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None
        self.buffer = b""

    def connection_made(self, transport):
        self.transport = transport
        self.transport.write(b"Rahul\nPython\n")

    def data_received(self, data):
        self.buffer += data

        while b"\n" in self.buffer:
            line, self.buffer = self.buffer.split(b"\n", 1)
            print("Complete message:", line.decode())

    def connection_lost(self, error):
        print("Connection closed")


async def handle_client(reader, writer):
    data = await reader.read(100)

    print("Server received:", data.decode())

    # Send the same data back.
    writer.write(data)
    await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main():
    # Start a local TCP echo server.
    server = await asyncio.start_server(
        handle_client,
        host="127.0.0.1",
        port=0,
    )

    address = server.sockets[0].getsockname()
    host, port = address[0], address[1]

    print(f"Server running on {host}:{port}")

    loop = asyncio.get_running_loop()

    result_future = loop.create_future()

    transport, protocol = await loop.create_connection(
        lambda: LineProtocol(
        ),
        host=host,
        port=port,
    )

    result = await result_future
    print("Final result:", result)

    server.close()
    await server.wait_closed()


asyncio.run(main())