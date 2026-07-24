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
    current = threading.current_thread()
    print("Current",current)
    print("ThreadName",current.name)

print("Threading count",threading.active_count())
# Wait until all orders are completed
for thread in threads:
    thread.join()

print("All orders are ready!")


#Custom Hook
def custom_hook(args):
    print("A thread crashed!")
    print("Thread:", args.thread.name)
    print("Exception type:", args.exc_type.__name__) # exc_type
    print("Exception message:", args.exc_value) # exc_value

threading.excepthook = custom_hook

def divide():
    print(10 / 0)  # Uncaught exception

worker = threading.Thread(
    target=divide,
    name="MathWorker"
)

worker.start()
print("Current thread:", threading.current_thread().name)
print("Python thread ID:", threading.get_ident())
worker.join()

print("Main thread continues")

# Example of Magic Cookie

thread_data = {}
lock = threading.Lock()

def process(user):
    thread_id = threading.get_ident()

    with lock:
        thread_data[thread_id] = {
            "thread": threading.current_thread().name,
            "user": user
        }

    time.sleep(1)

threads = [
    threading.Thread(target=process, args=("Rahul",), name="Worker-1"),
    threading.Thread(target=process, args=("Aman",), name="Worker-2"),
    threading.Thread(target=process, args=("Priya",), name="Worker-3"),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(thread_data)


# Example of lock
balance = 100
lock = threading.Lock()
def withdraw_balance(amount):
    global balance

    with lock:
        if balance > amount:
            print(
                f"{threading.current_thread().name} "
                f"is withdrawing ₹{amount}",
                threading.get_ident(),
                threading.get_native_id()
            )
            current_balance = balance
            time.sleep(0.1)
            balance = current_balance - amount
            print("Withdrawal successful")
        else:
            print(
                f"{threading.current_thread().name}: "
                "Insufficient balance"
            )

threads = [
    threading.Thread(target = withdraw_balance, args = (80,)),
    threading.Thread(target=withdraw_balance, args=(80,))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Final balance:", balance)


#Example of threading.enumerate()
def task():
    time.sleep(3)

threads = []

for number in range(3):
    thread = threading.Thread(
        target=task,
        name=f"Worker-{number + 1}"
    )
    threads.append(thread)
    thread.start()

active_threads = threading.enumerate()

for thread in active_threads:
    print(
        "Name:", thread.name,
        "| ident:", thread.ident,
        "| native ID:", thread.native_id,
        "| daemon:", thread.daemon
    )

for thread in threads:
    thread.join()


#Example of Trace call

def trace_calls(frame,event,arg):
    if event == "call":
        function_name = frame.f_code.co_name
        thread_name = threading.curre_thread().name

        print(
            f"{thread_name}",
            f"calling functio {function_name}"
        )
    return trace_calls

#Example of SetProfile

def profiler(frame, event, arg):
    function_name = frame.f_code.co_name
    thread_name = threading.current_thread().name

    if event == "call":
        print(f"[{thread_name}] Entering {function_name}()")

    elif event == "return":
        print(f"[{thread_name}] Leaving {function_name}()")

def downlaod():
    time.sleep(1)
    return "Downladed data "

def worker():
    data = downlaod()
    print(data)

# Apply profiler to subsequently created threads
threading.setprofile(profiler)

thread = threading.Thread(
    target=worker,
    name="DownloadWorker"
)

thread.start()
thread.join()

# Disable profiling for future threads
threading.setprofile(None)

# Another example for setprofile_for_all_event
start_times = {}
lock = threading.Lock()


def profiler(frame, event, arg):
    function_name = frame.f_code.co_name
    thread_id = threading.get_ident()

    if function_name not in {"download", "process"}:
        return

    key = (thread_id, id(frame))

    if event == "call":
        with lock:
            start_times[key] = time.perf_counter()

    elif event == "return":
        with lock:
            started = start_times.pop(key, None)

        if started is not None:
            elapsed = time.perf_counter() - started
            thread_name = threading.current_thread().name

            print(
                f"[{thread_name}] {function_name}() "
                f"took {elapsed:.3f} seconds"
            )


def download():
    time.sleep(1)


def process():
    time.sleep(0.5)


def worker():
    download()
    process()


threading.setprofile(profiler)

threads = [
    threading.Thread(target=worker, name="Worker-1"),
    threading.Thread(target=worker, name="Worker-2")
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

threading.setprofile(None)

#Example of threading.setprofile_all_threads(func)

stop_event = threading.Event()


def perform_work():
    time.sleep(0.1)


def existing_worker():
    while not stop_event.is_set():
        perform_work()


worker = threading.Thread(
    target=existing_worker,
    name="ExistingWorker"
)

# Start before installing the profiler
print("****setprofile_all_threads******")
worker.start()

time.sleep(0.3)


def profiler(frame, event, arg):
    if event == "call" and frame.f_code.co_name == "perform_work":
        print(
            f"[{threading.current_thread().name}] "
            "perform_work() called"
        )


# Also targets currently executing Python threads
threading.setprofile_all_threads(profiler)

time.sleep(0.5)

stop_event.set()
worker.join()

# threading.setprofile_all_threads(None)


# Write a programm to check how much time each function takes to execute
# It should include downloadData, processData and saveData

startTime = {}
threadLock = threading.Lock()



def download_data():
    time.sleep(2)
    print("Download completed!")

def process_data():
    time.sleep(3)
    print("Data Processed !")

def save_data():
    time.sleep(1)
    print("Data Saved !")

def worker():
    download_data()
    process_data()
    save_data()

threads=[
    threading.Thread(target=worker, name ="Dummy_worker")
]
monitored_functions = {
    "download_data",
    "process_data",
    "save_data"
}
def profile(frame,event,args):
    function_name = frame.f_code.co_name
    if function_name not in monitored_functions:
        return
    key = (threading.get_ident(), id(frame))

    if event == "call":
            with threadLock:
                start_times[key] = time.perf_counter()
    elif event == "return":
           end_time = time.perf_counter()

           with threadLock:
            start_time = start_times.pop(key,None)
            if start_time is not None:
                duration = end_time -start_time
                print(
                f"[{thread_name}] {function_name}() "
                f"took {elapsed_time:.2f} seconds"
            )

# Install the profiler before starting the threads
threading.setprofile_all_threads(profile)


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()

# Disable profiling
threading.setprofile_all_threads(None)

print("All tasks completed!")


# threading.getprofile() this gets the profiler function set by setProfile

print(threading.TIMEOUT_MAX)




        

        

