from multiprocessing import Process, Manager


def calculate_square(number, shared_results):
    result = number * number
    shared_results.append(result)
    print(f"Square of {number} is {result}")


if __name__ == "__main__":
    with Manager() as manager:
        # A list shared between all processes
        results = manager.list()

        processes = [
            Process(
                target=calculate_square,
                args=(number, results)
            )
            for number in range(1, 6)
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        print("Results:", list(results))