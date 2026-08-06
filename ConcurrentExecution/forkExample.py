import os
from multiprocessing import get_context
import multiprocessing

number = []

def worker():
    print("Child PID:", os.getpid())
    print("Parent PID:", os.getppid())
    number.append(200)
    print("Child:", number) #Guess the output

if __name__ == "__main__":
   
    multiprocessing.set_start_method("fork")
    number.append(100)

    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
    print("parent:", number) # Guess the Output
