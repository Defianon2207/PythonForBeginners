import multiprocessing


def deposit(balance):
    for _ in range(1000):
        with balance.get_lock():
            balance.value += 1


def withdraw(balance):
    for _ in range(500):
        with balance.get_lock():
            balance.value -= 1


if __name__ == "__main__":
    # "i" represents a signed integer
    balance = multiprocessing.Value("i", 10_000)

    processes = []

    # Create three deposit processes
    for _ in range(3):
        process = multiprocessing.Process(
            target=deposit,
            args=(balance,)
        )
        processes.append(process)

    # Create two withdrawal processes
    for _ in range(2):
        process = multiprocessing.Process(
            target=withdraw,
            args=(balance,)
        )
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes
    for process in processes:
        process.join()

    print("Final balance:", balance.value)