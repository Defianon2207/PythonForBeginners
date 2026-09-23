import asyncio
import socket


class ClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        transport.write(b"Hello")

    def data_received(self, data):
        print("Received:", data)
        self.transport.close()


async def main():
    raw_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )

    raw_socket.connect(("127.0.0.1", 8000))
    raw_socket.setblocking(False)

    loop = asyncio.get_running_loop()

    transport, protocol = await loop.create_connection(
        ClientProtocol,
        sock=raw_socket,
    )




asyncio.run(main())

#await loop.create_connection(
#     protocol_factory,
#     host="example.com",
#     port=443,
#     ssl=True,
#     ssl_shutdown_timeout=5,
# )