import threading
import time

products = []
condition = threading.Condition()


def consumer():
    with condition:
        # Keep checking because waking up doesn't guarantee
        # that a product is still available.
        while not products:
            print("Consumer: No product available. Waiting...")
            condition.wait()

        product = products.pop(0)
        print(f"Consumer: Consumed {product}")


def producer():
    time.sleep(2)

    with condition:
        product = "Laptop"
        products.append(product)
        print(f"Producer: Produced {product}")

        # Wake one waiting consumer
        condition.notify()


consumer_thread = threading.Thread(target=consumer)
producer_thread = threading.Thread(target=producer)

consumer_thread.start()
producer_thread.start()

consumer_thread.join()
producer_thread.join()

## Practice
# Create two threads:

# Producer: Adds numbers 1–5 to a shared list, one at a time.
# Consumer: Removes and prints numbers from the list.

# Rules:

# The consumer must wait using condition.wait() whenever the list is empty.
# The producer must call condition.notify() after adding an item.
# Both threads must access the shared list inside with condition:.
# Stop the consumer after it consumes all five numbers.

N_list = []

def n_consumer():
    print("Consumer triggered")
    for _ in range(5):
        with condition:
            while not N_list:
                condition.wait()
            number =  N_list.pop()
            print(f"Consumed: {number} ")
           

def n_producer():
        k =1
        while k < 6:
            time.sleep(1)
            with condition:
                N_list.append(k)
                print(f"Produced: {k}")
                condition.notify()
            k = k+1

            
thread1 = threading.Thread(target=n_producer)
thread2 = threading.Thread(target=n_consumer)

thread2.start()
thread1.start()
thread1.join()
thread2.join()


## Example of multiple consumer 

numbers = []
condition = threading.Condition()


def consumer(name):
    with condition:
        print(f"{name}: waiting for a number")

        available = condition.wait_for(
            lambda: len(numbers) > 0,
            timeout=5
        )

        if not available:
            print(f"{name}: timed out")
            return

        number = numbers.pop(0)
        print(f"{name}: consumed {number}")


def producer():
    time.sleep(2)

    with condition:
        numbers.extend([10, 20])
        print("Producer: produced 10 and 20")

        condition.notify_all()


thread1 = threading.Thread(target=consumer, args=("Consumer 1",))
thread2 = threading.Thread(target=consumer, args=("Consumer 2",))
thread3 = threading.Thread(target=producer)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

# Example for notified

# def consumer():
#     with condition:
#         while not numbers:
#             print("Waiting...")
#             notified = condition.wait(timeout=3)

#             if not notified:
#                 print("Timed out")
#                 return

# acquire()    → lock the shared state
# release()    → unlock the shared state
# locked()     → check whether it is locked
# wait()       → unlock, sleep, then lock again
# wait_for()   → wait until a predicate becomes true
# notify()     → wake one or n waiters
# notify_all() → wake every waiter




