from multiprocessing import Process, Queue, Pipe

def worker(queue):
    data = queue.get()
    data.append(4)
    print("Child:", data)

def child_work(connection):
    message = connection.recv()
    print("Child received:", message)

    connection.send("Hello from child")
    connection.close()

def producer(queue):
    for _ in range(1,6):
        queue.put(_)

def consumer(queue):
    for _ in range(1,6):
        print("Consumed :",queue.get())


if __name__ == "__main__":
    queue = Queue()
    original = [1, 2, 3]

    queue.put(original)

    process = Process(target=worker, args=(queue,))
    process.start()
    process.join()

    print("Parent:", original)

    parent_conn, child_conn = Pipe()
    process = Process(
        target =child_work,
        args =(child_conn,)
    )
    process.start()
    child_conn.close()

    parent_conn.send("Hello from parent")

    response = parent_conn.recv()
    print("Parent received:", response)

    parent_conn.close()
    process.join()

# receiving_conn, sending_conn = Pipe(duplex=False)

# When duplex=False:

# The first connection can only receive.
# The second connection can only send.

    queue = Queue()

    process = [Process(
        target = producer,
        args =(queue,)
    ), Process(
        target = consumer,
        args =(queue,)
    )]

    process[0].start()
    process[1].start()
    process[0].join()
    process[1].join()
    queue.close()
    queue.join_thread()
