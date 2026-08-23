from multiprocessing import Process, Value
from multiprocessing import Array


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

    numbers = Array("i", [10, 20, 30, 40])

    print(numbers[:])  # [10, 20, 30, 40]

    numbers[1] = 99

    print(numbers[:])  # [10, 99, 30, 40]