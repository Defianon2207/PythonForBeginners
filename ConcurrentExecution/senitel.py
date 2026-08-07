from multiprocessing import Process
from multiprocessing.connection import wait
import time

def worker(number, delay):
    time.sleep(delay)
    print(f"Worker {number} finished")

if __name__ == "__main__":
    processes = [
        Process(target=worker, args=(1, 3)),
        Process(target=worker, args=(2, 1)),
        Process(target=worker, args=(3, 2))
    ]

    for process in processes:
        process.start()

    sentinel_to_process = {
        process.sentinel: process
        for process in processes
    }

    while sentinel_to_process:
        ready_sentinels = wait(sentinel_to_process)

        for sentinel in ready_sentinels:
            process = sentinel_to_process.pop(sentinel)
            process.join()

            print(
                process.name,
                "ended with",
                process.exitcode
            )


#             from multiprocessing import Pipe, BufferTooShort

# if __name__ == "__main__":
#     receiving_conn, sending_conn = Pipe(duplex=False)

#     sending_conn.send_bytes(b"Hello, this message is long")

#     small_buffer = bytearray(5)

#     try:
#         receiving_conn.recv_bytes_into(small_buffer)
#     except BufferTooShort as error:
#         complete_message = error.args[0]

#         print("Buffer was too small")
#         print("Complete message:", complete_message)

#     receiving_conn.close()
    # sending_conn.close()