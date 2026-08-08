from multiprocessing import Process, Queue
import time
from queue import Full

def producer(queue, label):
    for number in range(3):
        queue.put(f"{label}-{number}")
        time.sleep(0.01)

if __name__ == "__main__":
    queue = Queue()

    p1 = Process(target=producer, args=(queue, "A"))
    p2 = Process(target=producer, args=(queue, "B"))

    p1.start()
   
    p2.start()

    for _ in range(6):
        print(queue.empty())
        print(queue.get())

    p1.join()
    p2.join()

    queue = Queue(maxsize=1)
    queue.put("First")

    try:
        queue.put("Second", timeout=2)
    except Full:
        print("No free slot became available")

    queue = Queue(maxsize=1)
    queue.put_nowait("First")

    try:
        queue.put_nowait("Second")
    except Full:
        print("Queue is full")

# SimpleQueue is a simpler queue implementation, roughly resembling a locked pipe.
# def producer(queue):
#     queue.put("Hello")
#     queue.put([1, 2, 3])

# if __name__ == "__main__":
#     queue = SimpleQueue()

#     process = Process(target=producer, args=(queue,))
#     process.start()

#     print(queue.get())
#     print(queue.get())

#     process.join()
#     queue.close()

# queue.put(item)
# queue.get()
# queue.empty()
# queue.close()