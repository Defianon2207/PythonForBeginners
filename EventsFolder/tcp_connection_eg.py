import asyncio


class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, result_future):
        self.message = message
        self.result_future = result_future
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

        print("Connection established")

        data = self.message.encode()
        print("Sending:", self.message)

        transport.write(data)

    def data_received(self, data):
        message = data.decode()

        print("Received:", message)

        if not self.result_future.done():
            self.result_future.set_result(message)

        self.transport.close()

    def connection_lost(self, error):
        if error is None:
            print("Connection closed normally")
        else:
            print("Connection failed:", error)

            if not self.result_future.done():
                self.result_future.set_exception(error)


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
        lambda: EchoClientProtocol(
            "Hello from client",
            result_future,
        ),
        host=host,
        port=port,
    )

    result = await result_future
    print("Final result:", result)

    server.close()
    await server.wait_closed()


asyncio.run(main())