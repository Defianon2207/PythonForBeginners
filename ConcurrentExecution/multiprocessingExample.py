from multiprocessing import Pool, Process, get_context
import os
import multiprocessing


def f(x):
    return x*x

def fpro(name):
    print(f"Name is : {name}")

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f2(name):
    info('function f2')
    print('hello', name)

#Spawn example
number = 10

def spawnWorker():
    print("spawn PID :",os.getpid(), os.getppid())
    print("Number:", number)

# With spawn, Python starts a completely new Python interpreter.

# Parent Python process
#         │
#         └── Starts fresh Python interpreter
#                     │
#                     └── Imports program and runs target
numbers = []

def worker():
    print(numbers)


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")

    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

    p = Process(target =fpro, args=("Defianon",))
    p.start()
    p.join()
    info('main line')
    p = Process(target=f2, args=('bob',))
    p.start()
    p.join()
    #Spawn Example

    # ctx = get_context("spawn")
    # p = ctx.Process(target=spawnWorker)
    # p.start()
    # p.join()
#Using get_start_method()
 
    numbers.append(100)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()