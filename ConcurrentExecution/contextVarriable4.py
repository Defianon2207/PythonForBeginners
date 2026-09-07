import asyncio
from contextvars import ContextVar

client_address = ContextVar("client_address")


def create_response():
    address = client_address.get()

    body = f"Goodbye, client at {address}\n".encode()

    return (
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: text/plain\r\n"
        + f"Content-Length: {len(body)}\r\n".encode()
        + b"Connection: close\r\n"
        + b"\r\n"
        + body
    )


async def handle_request(reader, writer):
    address = writer.get_extra_info("peername")

    with client_address.set(address):
        await reader.read(4096)

        writer.write(create_response())
        await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        handle_request,
        host="127.0.0.1",
        port=8081,
    )

    print("Server running at http://127.0.0.1:8081")

    async with server:
        await server.serve_forever()


asyncio.run(main())