import threading
import time

server_ready = threading.Event()


def worker(name):
    print(f"{name}: Waiting for the server...")

    server_ready.wait()

    print(f"{name}: Server is ready. Starting work.")


def start_server():
    print("Server: Starting...", server_ready.is_set())
    time.sleep(3)

    server_ready.set()
    print("Server: Ready!",server_ready.is_set())


threads = [
    threading.Thread(target=worker, args=(f"Worker {i}",))
    for i in range(1, 4)
]

for thread in threads:
    thread.start()

server_thread = threading.Thread(target=start_server)
server_thread.start()

for thread in threads:
    thread.join()

server_thread.join()


#Example of timer
def hello():
    print("Hello, world!")


timer = threading.Timer(3, hello)
timer.start()

print("Timer started")

# Wait for the timer thread to finish
timer.join()

print("Program finished")