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



