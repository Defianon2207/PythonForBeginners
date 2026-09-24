import asyncio


class UDPServerProtocol(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        self.transport = transport

        address = transport.get_extra_info("sockname")
        print("UDP server running on:", address,type(self.transport),"Above this", sep ="\n")

    def datagram_received(self, data, address):
        message = data.decode()

        print(f"Server received {message!r} from {address}")

        # Send the same datagram back to its sender.
        self.transport.sendto(data, address)

    def error_received(self, error):
        print("Server error:", error)

    def connection_lost(self, error):
        print("Server endpoint closed")


class UDPClientProtocol(asyncio.DatagramProtocol):
    def __init__(self, message, result_future):
        self.message = message
        self.result_future = result_future
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

        print("Client endpoint created")
        print("Client sending:", self.message)

        self.transport.sendto(self.message.encode())

    def datagram_received(self, data, address):
        message = data.decode()

        print(f"Client received {message!r} from {address}")

        if not self.result_future.done():
            self.result_future.set_result(message)

        self.transport.close()

    def error_received(self, error):
        print("Client error:", error)

        if not self.result_future.done():
            self.result_future.set_exception(error)

    def connection_lost(self, error):
        print("Client endpoint closed")


async def main():

    loop = asyncio.get_running_loop()
    print(loop,"The name of the loop")
    # Create the UDP server.
    server_transport, server_protocol = (
        await loop.create_datagram_endpoint(
            UDPServerProtocol,
            local_addr=("127.0.0.1", 0),
        )
    )

    # Find the port selected by the operating system.
    server_address = server_transport.get_extra_info("sockname")
    print("Server address:", server_address)

    result_future = loop.create_future()

    # Create the UDP client.
    client_transport, client_protocol = (
        await loop.create_datagram_endpoint(
            lambda: UDPClientProtocol(
                "Hello over UDP",
                result_future,
            ),
            remote_addr=server_address,
        )
    )

    try:
        result = await asyncio.wait_for(
            result_future,
            timeout=5,
        )

        print("Final result:", result)

    finally:
        client_transport.close()
        server_transport.close()

        # Give connection_lost() callbacks a chance to run.
        await asyncio.sleep(0)


asyncio.run(main())