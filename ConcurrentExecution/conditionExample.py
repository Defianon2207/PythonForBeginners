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