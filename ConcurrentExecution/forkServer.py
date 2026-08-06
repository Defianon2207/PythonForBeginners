import os
from multiprocessing import get_context

def worker():
    print("Worker PID:", os.getpid())
    print("Worker parent PID:", os.getppid())

if __name__ == "__main__":
    ctx = get_context("forkserver")

    p = ctx.Process(target=worker)
    p.start()
    p.join()