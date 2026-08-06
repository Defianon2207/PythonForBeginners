import os
from multiprocessing import get_context

number = 10

def worker():
    print("Child PID:", os.getpid())
    print("Parent PID:", os.getppid())
    print("Number:", number)

if __name__ == "__main__":
    ctx = get_context("fork")

    p = ctx.Process(target=worker)
    p.start()
    p.join()
    