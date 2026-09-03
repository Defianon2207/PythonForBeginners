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


# Map function example
def square(a):
    return a**2

with ThreadPoolExecutor(max_workers=4) as executor:
    future = executor.map(square,[2,3,4,5,6])

    print("square result",list(future))




#     5. Useful Future methods
# future.done()

# Checks whether the task has finished:

# print(future.done())

# It returns True or False.

# future.running()

# Checks whether the task is currently running:

# print(future.running())
# future.cancel()

# Attempts to cancel the task:

# cancelled = future.cancel()

# Cancellation succeeds only if the executor has not started running the task.

# future.cancelled()

# Checks whether it was successfully cancelled:

# print(future.cancelled())
# future.exception()

# Returns the exception raised by the task:

# error = future.exception()

# It returns None if the task completed successfully.

# 6. Handling exceptions from submit()
