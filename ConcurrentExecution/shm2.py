from multiprocessing import Process
from multiprocessing import shared_memory


def worker(shm_name):
    # Connect to the block created by the parent
    shm = shared_memory.SharedMemory(name=shm_name)

    try:
        print("Worker received:", list(shm.buf[:5]))

        for index in range(5):
            shm.buf[index] *= 2

    finally:
        # Worker closes only its own handle
        shm.close()


if __name__ == "__main__":
    shm = shared_memory.SharedMemory(create=True, size=5)

    try:
        shm.buf[:5] = bytes([10, 20, 30, 40, 50])

        process = Process(target=worker, args=(shm.name,))
        process.start()
        process.join()

        print("Parent sees:", list(shm.buf[:5]))

    finally:
        shm.close()
        shm.unlink()