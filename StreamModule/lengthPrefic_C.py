import asyncio

async def main():
    reader, writer = await asyncio.open_connection(
        "127.0.0.1",
        8888,
    )

    try:
        message = "Hello from the client"
        data = message.encode()

        header = len(data).to_bytes(
            4,
            byteorder="big",
        )

        writer.write(header + data)
        await writer.drain()

        response = await reader.readexactly(2)
        print(response.decode())

    finally:
        writer.close()
        await writer.wait_closed()

asyncio.run(main())


#keep a note of this 
#data = await reader.readuntil(separator)

# If the stream contains:
# b"Hello World<END>Remaining data"
# the result is:
# b"Hello World<END>"