from multiprocessing import shared_memory

shm = shared_memory.SharedMemory(create=True, size=10)

print("Shared Memory Name:",shm.name)
print(type(shm.buf))
print(len(shm.buf))
shm.buf[0] = 10
shm.buf[1] = 20
shm.buf[2] = 30
print(list(shm.buf[:3]))

## Two handles accessing the same block
shm_a = shared_memory.SharedMemory(create=True, size=10)
shm_a.buf[:5] = b"hello"

shm_b = shared_memory.SharedMemory(name=shm_a.name)

print(bytes(shm_b.buf[:5]))

shm_b.buf[:5] = b"howdy"

print(bytes(shm_a.buf[0]))

shm_b.close()
shm_a.close()
shm_a.unlink()