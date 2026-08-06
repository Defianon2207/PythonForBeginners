import os
from multiprocessing import get_context
import multiprocessing

number = []

def worker():
    print("Child PID:", os.getpid())
    print("Parent PID:", os.getppid())
    print("Number:", number)
    number.append(200)
    print("Child:", number)

if __name__ == "__main__":
    # ctx = get_context("fork")

    # p = ctx.Process(target=worker)
    # p.start()
    # p.join()
    multiprocessing.set_start_method("fork")
    number.append(100)

    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
    print("parent Number:", number)
