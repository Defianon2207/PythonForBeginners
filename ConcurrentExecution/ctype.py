from multiprocessing import Process, Value


def increment_counter(counter):
    for _ in range(10_000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    # "i" means signed integer, initially set to 0
    counter = Value("i", 0)

    processes = []

    for _ in range(4):
        process = Process(
            target=increment_counter,
            args=(counter,)
        )
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print("Final counter:", counter.value)