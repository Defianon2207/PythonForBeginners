import asyncio
import os


async def main():
    loop = asyncio.get_running_loop()

    # Create an operating-system pipe.
    read_fd, write_fd = os.pipe()

    # Ensure reading never blocks.
    os.set_blocking(read_fd, False)

    finished = loop.create_future()

    def on_data_available(fd):
        try:
            data = os.read(fd, 1024)

            if data:
                print("Received:", data.decode())

            else:
                # b"" means the write end was closed.
                print("End of pipe")

                removed = loop.remove_reader(fd)
                print("Reader removed:", removed)

                os.close(fd)

                if not finished.done():
                    finished.set_result(None)

        except BlockingIOError:
            # No data is currently available.
            pass

    # Start watching the read end.
    loop.add_reader(
        read_fd,
        on_data_available,
        read_fd,
    )

    def write_message():
        print("Writing into pipe")

        os.write(
            write_fd,
            b"Hello from the pipe!",
        )

        # Closing the writer eventually causes os.read()
        # to return b"" after all buffered data is read.
        os.close(write_fd)

    # Write after one second.
    loop.call_later(1, write_message)

    print("Waiting for pipe data...")

    await finished

    print("Program finished")


asyncio.run(main())