from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

def worker(q):
    original = [1, 2, 3]
    q.put(original)

if __name__ == '__main__':
    q = Queue()

    p = Process(target=f, args=(q,))
    p.start()

    print(q.get())
    p.join()

    p = Process(target=worker, args=(q,))
    p.start()

    received = q.get()
       # item = q.get(timeout=2) you can add timeout of the if object is not available
    print(received)

    p.join()
    # print(q.get())

   