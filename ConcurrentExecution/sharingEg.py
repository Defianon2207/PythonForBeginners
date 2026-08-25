from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

def increment(counter):
    for _ in range(100_000):
        with counter.get_lock():
            counter.value += 1

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
    counter = Value("i", 0)

    processes = [
        Process(target=increment, args=(counter,))
        for _ in range(4)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(counter.value)

