# Create a Python program using multiprocessing that:

# Creates a shared integer using multiprocessing.Value, initially set to 0.
# Starts 5 processes.
# Each process increments the shared value 1,000 times.
# Prevents race conditions using the shared value’s lock.
# Waits for all processes to finish.
# Prints the final value.
import multiprocessing

def increment_number(number):
    for _ in range(1000):
        with number.get_lock():
            number.value += 1


if __name__ == "__main__":
    # Shared integer initially set to 0
    number = multiprocessing.Value("i", 0)

    processes = []

    # Create and start 5 processes
    for _ in range(5):
        process = multiprocessing.Process(
            target=increment_number,
            args=(number,)
        )
        process.start()
        processes.append(process)

    # Wait for every process to finish
    for process in processes:
        process.join()

    print("Final number:", number.value)

