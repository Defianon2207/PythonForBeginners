from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

def worker1(q):
    original = [1, 2, 3]
    q.put(original)

def worker(number, results):
    results.put(number * number)

if __name__ == '__main__':
    q = Queue()

    p = Process(target=f, args=(q,))
    p.start()

    print(q.get())
    p.join()

    p = Process(target=worker1, args=(q,))
    p.start()

    received = q.get()
       # item = q.get(timeout=2) you can add timeout of the if object is not available
    print(received)

    p.join()
    # print(q.get())

#    A queue follows FIFO ordering:

# First In, First Out

# Example:

# q.put("A")
# q.put("B")
# q.put("C")

# print(q.get())  # A
# print(q.get())  # B
# print(q.get())  # C

# With multiple producer processes, the messages from 
# any one producer retain their order, but messages from different producers can interleave depending on timing.

    results = Queue()
    processes = []

    for number in [1, 2, 3]:
        p = Process(target=worker, args=(number, results))
        p.start()
        processes.append(p)

    for _ in processes:
        print(results.get())

    for p in processes:
        p.join()