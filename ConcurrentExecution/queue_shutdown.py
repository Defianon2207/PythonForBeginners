from queue import Queue, ShutDown
from threading import Thread
import time


def worker(tasks):
    while True:
        try:
            task = tasks.get()
        except ShutDown:
            print("Queue is empty and shut down. Worker exiting.")
            break

        try:
            print(f"Processing {task}")
            time.sleep(1)
            print(f"Finished {task}")
        finally:
            tasks.task_done()


tasks = Queue()

worker_thread = Thread(target=worker,args=(tasks,))
worker_thread.start()

for item in ["A", "B", "C"]:
    tasks.put(item)

# Stop accepting new tasks, but allow A, B and C to be processed.
tasks.shutdown()

tasks.join()
worker_thread.join()

print("All queued tasks completed.")