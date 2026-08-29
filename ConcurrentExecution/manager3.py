from multiprocessing import Process, Manager


def increment(counter, lock):
    for _ in range(10_000):
        with lock:
            counter["value"] += 1


if __name__ == "__main__":
    with Manager() as manager:
        counter = manager.dict(value=0)
        lock = manager.Lock()

        processes = [
            Process(target=increment, args=(counter, lock))
            for _ in range(4)
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        print(counter["value"])