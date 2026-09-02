from multiprocessing import shared_memory

shm = shared_memory.SharedMemory(create=True, size=10)

print("Shared Memory Name:",shm.name)
print(type(shm.buf))
print(len(shm.buf))
shm.buf[0] = 10
shm.buf[1] = 20
shm.buf[2] = 30
print(list(shm.buf[:3]))