import asyncio


class FileServerProtocol(asyncio.Protocol):
    def __init__(self, file_path, finished_future):
        self.file_path = file_path
        self.finished_future = finished_future
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

        client_address = transport.get_extra_info("peername")
        print("Client connected:", client_address)

        # connection_made() cannot use await directly,
        # so create a Task for the async send operation.
        asyncio.create_task(self.send_file())

    async def send_file(self):
        loop = asyncio.get_running_loop()

        try:
            # The file must be opened in binary mode.
            with open(self.file_path, "rb") as file:
                bytes_sent = await loop.sendfile(
                    self.transport,
                    file,
                )

                print("Server sent:", bytes_sent, "bytes")
                print("Final file position:", file.tell())

            if not self.finished_future.done():
                self.finished_future.set_result(bytes_sent)

        except Exception as error:
            if not self.finished_future.done():
                self.finished_future.set_exception(error)

        finally:
            self.transport.close()

    def connection_lost(self, error):
        if error is None:
            print("Server connection closed normally")
        else:
            print("Server connection error:", error)


async def download_file(host, port):
    reader, writer = await asyncio.open_connection(host, port)

    received_data = bytearray()

    while True:
        chunk = await reader.read(64 * 1024)

        if not chunk:
            break

        received_data.extend(chunk)

    writer.close()
    await writer.wait_closed()

    print("Client received:", len(received_data), "bytes")

    return bytes(received_data)


async def main():
    file_path = "example.txt"

    # Create an example binary file.
    with open(file_path, "wb") as file:
        file.write(b"Hello Rahul!\n")
        file.write(b"This file was transferred using asyncio.sendfile().\n")

    loop = asyncio.get_running_loop()
    finished_future = loop.create_future()

    server = await loop.create_server(
        lambda: FileServerProtocol(
            file_path,
            finished_future,
        ),
        host="127.0.0.1",
        port=0,
    )

    host, port = server.sockets[0].getsockname()[:2]
    print(f"Server running on {host}:{port}")

    received_data = await download_file(host, port)
    bytes_sent = await finished_future

    print("Final result:", received_data.decode())
    print("Bytes reported by sendfile():", bytes_sent)

    server.close()
    await server.wait_closed()


# asyncio.run(main())

# Client connects
#       ↓
# connection_made(transport)
#       ↓
# create_task(self.send_file())
#       ↓
# send_file() opens the file
#       ↓
# await loop.sendfile(transport, file)
#       ↓
# File bytes travel through TCP
#       ↓
# Transport closes