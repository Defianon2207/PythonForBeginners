from multiprocessing import Process, Value


def increase(counter, repetitions):
    for _ in range(repetitions):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value("i", 0)

    processes = [
        Process(target=increase, args=(counter, 100_000))
        for _ in range(4)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(counter.value)  # 400000