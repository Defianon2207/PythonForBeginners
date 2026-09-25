import asyncio
import ssl


class StartTLSServerProtocol(asyncio.Protocol):
    def __init__(self, ssl_context):
        self.ssl_context = ssl_context
        self.transport = None
        self.tls_active = False
        self.upgrading = False

    def connection_made(self, transport):
        self.transport = transport

        client = transport.get_extra_info("peername")
        print("Server: client connected:", client)

        self.transport.write(
            b"Welcome. Send STARTTLS to enable encryption.\n"
        )

    def data_received(self, data):
        message = data.decode().strip()
        print("Server received:", message)

        if message == "STARTTLS" and not self.tls_active:
            if self.upgrading:
                return

            self.upgrading = True

            # This response is still plaintext.
            self.transport.write(b"READY\n")

            asyncio.create_task(self.enable_tls())

        elif self.tls_active:
            response = f"Secure echo: {message}\n"
            self.transport.write(response.encode())

        else:
            self.transport.write(
                b"Encryption required. Send STARTTLS.\n"
            )

    async def enable_tls(self):
        loop = asyncio.get_running_loop()

        old_transport = self.transport

        try:
            new_transport = await loop.start_tls(
                old_transport,
                self,
                self.ssl_context,
                server_side=True,
                ssl_handshake_timeout=10,
                ssl_shutdown_timeout=5,
            )

            if new_transport is None:
                print("Server: connection closed during TLS upgrade")
                return

            # Stop using old_transport.
            self.transport = new_transport
            self.tls_active = True

            print("Server: TLS enabled")

        except Exception as error:
            print("Server TLS upgrade failed:", error)
            old_transport.close()

    def connection_lost(self, error):
        if error is None:
            print("Server: connection closed")
        else:
            print("Server connection error:", error)


class StartTLSClientProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None
        self.ready_future = None
        self.response_future = None
        self.tls_active = False

    def connection_made(self, transport):
        self.transport = transport
        print("Client: plaintext connection established")

    def data_received(self, data):
        message = data.decode().strip()
        print("Client received:", message)

        if message.startswith("Welcome"):
            print("Client: requesting TLS")
            self.transport.write(b"STARTTLS\n")

        elif message == "READY":
            if not self.ready_future.done():
                self.ready_future.set_result(True)

        elif message.startswith("Secure echo:"):
            if not self.response_future.done():
                self.response_future.set_result(message)

    def connection_lost(self, error):
        if error is None:
            print("Client: connection closed")
        else:
            print("Client connection error:", error)

            if (
                self.response_future is not None
                and not self.response_future.done()
            ):
                self.response_future.set_exception(error)


async def main():
    loop = asyncio.get_running_loop()

    # Server TLS configuration
    server_ssl_context = ssl.SSLContext(
        ssl.PROTOCOL_TLS_SERVER
    )

    server_ssl_context.load_cert_chain(
        certfile="certificate.pem",
        keyfile="key.pem",
    )

    server = await loop.create_server(
        lambda: StartTLSServerProtocol(server_ssl_context),
        host="127.0.0.1",
        port=0,
    )

    host, port = server.sockets[0].getsockname()[:2]
    print(f"Server running on {host}:{port}")

    # Client TLS configuration
    client_ssl_context = ssl.create_default_context()

    # Development only: trust our self-signed certificate.
    client_ssl_context.load_verify_locations(
        cafile="certificate.pem"
    )

    client_protocol = StartTLSClientProtocol()
    client_protocol.ready_future = loop.create_future()
    client_protocol.response_future = loop.create_future()

    original_transport, protocol = await loop.create_connection(
        lambda: client_protocol,
        host=host,
        port=port,
    )

    try:
        # Wait until the server responds with READY.
        await asyncio.wait_for(
            client_protocol.ready_future,
            timeout=5,
        )

        print("Client: beginning TLS handshake")

        tls_transport = await loop.start_tls(
            original_transport,
            protocol,
            client_ssl_context,
            server_side=False,
            server_hostname="localhost",
            ssl_handshake_timeout=10,
            ssl_shutdown_timeout=5,
        )

        if tls_transport is None:
            raise ConnectionError(
                "Connection closed during TLS upgrade"
            )

        # Important: replace the original Transport.
        client_protocol.transport = tls_transport
        client_protocol.tls_active = True

        print("Client: TLS enabled")

        # This message is encrypted.
        tls_transport.write(b"Hello through TLS\n")

        response = await asyncio.wait_for(
            client_protocol.response_future,
            timeout=5,
        )

        print("Final response:", response)

    finally:
        client_protocol.transport.close()

        server.close()
        await server.wait_closed()


asyncio.run(main())

# Server running on 127.0.0.1:51234
# Server: client connected: ('127.0.0.1', 51235)
# Client: plaintext connection established
# Client received: Welcome. Send STARTTLS to enable encryption.
# Client: requesting TLS
# Server received: STARTTLS
# Client received: READY
# Client: beginning TLS handshake
# Client: TLS enabled
# Server: TLS enabled
# Server received: Hello through TLS
# Client received: Secure echo: Hello through TLS
# Final response: Secure echo: Hello through TLS

# start_tls() versus creating TLS immediately

# If encryption is required from the beginning, use the ssl argument of create_connection():

# transport, protocol = await loop.create_connection(
#     protocol_factory,
#     host="example.com",
#     port=443,
#     ssl=ssl.create_default_context(),
#     server_hostname="example.com",
# )