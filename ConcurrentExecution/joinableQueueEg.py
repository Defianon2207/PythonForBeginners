from multiprocessing import Process, JoinableQueue
import time

STOP = None

def worker(tasks):
    while True:
        task = tasks.get()

        try:
            if task is STOP:
                return

            print(f"Processing {task}", flush=True)
            time.sleep(1)
            print(f"Finished {task}", flush=True)

        finally:
            tasks.task_done()

if __name__ == "__main__":
    tasks = JoinableQueue()
    workers = []

    for _ in range(2):
        process = Process(target=worker, args=(tasks,))
        process.start()
        workers.append(process)

    for task in ["A", "B", "C", "D"]:
        tasks.put(task)

    # Wait until A, B, C and D are processed.
    tasks.join()

    # Send one stop message to each worker.
    for _ in workers:
        tasks.put(STOP)

    # Wait until stop messages are acknowledged.
    tasks.join()

    for process in workers:
        process.join()

    tasks.close()
    tasks.join_thread()

    print("Everything completed")