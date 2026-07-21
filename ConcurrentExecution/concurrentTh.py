import threading
import time

def crawl(link, delay=3):
    print(f"crawl started for {link}")
    time.sleep(delay)
    print(f"crawl ended for {link}")

links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

start_time = time.perf_counter()

threads = []

for link in links:
    thread = threading.Thread(
        target=crawl,
        args=(link,),
        kwargs={"delay": 2}
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

elapsed = time.perf_counter() - start_time

print(f"Completed in {elapsed:.2f} seconds")


#Example 2
def prepare_order(customer, delay):
    print(f"Started preparing order for {customer}")

    # Simulates waiting for an external operation
    time.sleep(delay)

    print(f"Finished preparing order for {customer}")


customers = ["Rahul", "Aman", "Priya"]
threads = []

# Create one thread for each customer
for customer in customers:
    thread = threading.Thread(
        target=prepare_order,
        args=(customer, 2)
    )
    threads.append(thread)

# Start all orders
for thread in threads:
    thread.start()

# Wait until all orders are completed
for thread in threads:
    thread.join()

print("All orders are ready!")