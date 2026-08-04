import threading
import time
import random

# Only three workers may use the database simultaneously.
database_slots = threading.Semaphore(3)


def access_database(worker_name):
    print(f"{worker_name}: waiting for a connection")

    with database_slots:
        # acquire() is called automatically here
        print(f"{worker_name}: connection acquired")

        time.sleep(random.randint(2, 4))

        print(f"{worker_name}: finished using database")

    # release() is called automatically here


threads = []

for number in range(1, 7):
    thread = threading.Thread(
        target=access_database,
        args=(f"Worker {number}",)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All workers finished")


#Semaphore todo example
# A parking lot has only 3 parking spaces, but 6 cars arrive at the same time.

# Write a Python program using threading.Semaphore so that:

# Only 3 cars can park at a time.
# Each car stays for 2 seconds.
# When one car leaves, another waiting car can enter.