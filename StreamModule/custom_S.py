import asyncio

SEPARATOR = b"<END>"

async def handle_client(reader, writer):
    try:
        while True:
            data = await reader.readuntil(SEPARATOR)

            message = data.removesuffix(SEPARATOR).decode()
            print("Received:", message)

            writer.write(b"ACK<END>")
            await writer.drain()

    except asyncio.IncompleteReadError as error:
        if error.partial:
            print("Incomplete message:", error.partial)

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

#Note 
#Starting with Python 3.13, separator may be a tuple:
# data = await reader.readuntil(
#     (b"\n", b"\r\n", b"<END>")
# )

#LIMITOverrunError

# reader, writer = await asyncio.open_connection(
#     "127.0.0.1",
#     8888,
#     limit=1024,
# )