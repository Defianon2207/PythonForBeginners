#Just an example Numpy not installed
from multiprocessing import Process, shared_memory
import numpy as np


def double_numbers(shm_name, shape, dtype_string):
    shm = shared_memory.SharedMemory(name=shm_name)

    try:
        dtype = np.dtype(dtype_string)

        shared_array = np.ndarray(
            shape,
            dtype=dtype,
            buffer=shm.buf
        )

        shared_array *= 2

    finally:
        shm.close()


if __name__ == "__main__":
    original = np.array([1, 2, 3, 4], dtype=np.int64)

    shm = shared_memory.SharedMemory(
        create=True,
        size=original.nbytes
    )

    try:
        shared_array = np.ndarray(
            original.shape,
            dtype=original.dtype,
            buffer=shm.buf
        )

        shared_array[:] = original

        process = Process(
            target=double_numbers,
            args=(
                shm.name,
                original.shape,
                original.dtype.str
            )
        )

        process.start()
        process.join()

        print(shared_array)

    finally:
        shm.close()
        shm.unlink()


#Example of shareable 
# values = shared_memory.ShareableList([100, 200])

# values[0] = 3.14
# values[1] = "hello"

# print(list(values))

# A ShareableList cannot change length