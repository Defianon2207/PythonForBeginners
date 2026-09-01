from multiprocessing import Process, Manager
import time


def worker(start_event):
    print("Worker is waiting")

    start_event.wait()

    print("Worker has started")


if __name__ == "__main__":
    with Manager() as manager:
        start_event = manager.Event()

        process = Process(
            target=worker,
            args=(start_event,)
        )

        process.start()

        time.sleep(2)
        start_event.set()

        process.join()