from concurrent.futures import ThreadPoolExecutor
import time


def add(a, b):
    return a + b


with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(add, 10, 20)

    print(future)
    print(future.result())


def create_user(name, active=False):
    return f"{name}: active={active}"


with ThreadPoolExecutor() as executor:
    future = executor.submit(
        create_user,
        name="Rahul",
        active=True
    )

    print(future.result())

def slow_task():
    print("Task started")
    time.sleep(3)
    print("Task finished")
    return 100

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(slow_task)

    print("Task submitted")
    print("Main program can do other work")

    result = future.result()
    print("Result:", result)