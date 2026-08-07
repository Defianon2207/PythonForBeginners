import os
from multiprocessing import Process,Queue
import traceback

def welcome(name,greetings):
    print(os.getpid())
    print(f"{greetings}, {name}")

def worker(number):
    print("PID:", os.getpid(), os.getppid())
    print("Square:", number * number)

def grandchild_work():
    print("Grandchild working")

def daemon_worker():
    child = Process(target=grandchild_work)
    child.start()  # Fails
    child.join()

def worker2(errors):
    try:
        result = 10 / 0
    except Exception:
        errors.put(traceback.format_exc())

if __name__ == "__main__":
    process = Process(
        target = welcome,
        args=("Rahul","Namaste"),
        name="Welcome Function",
        daemon=False
    )
    process.start()
    print(process.is_alive())
    process.join()
    print(process.is_alive())

    process = Process(target=worker, args=(5,))
    print(os.getpid())
    process.run()

# !! ****Important**** !!
# if __name__ == "__main__":
#     print("Main PID:", os.getpid())

#     p1 = Process(target=worker)
#     p1.run()  # Same process

#     p2 = Process(target=worker)
#     p2.start()  # Separate process
#     p2.join()

# Example of Daemon 
    process = Process(
        target=daemon_worker,
        daemon=False  #If you make this false it wont run
    )

    process.start()
    process.join()

#     exitcode
# The child’s exit code. This will be None if the process has not yet terminated.

# If the child’s run() method returned normally, the exit code will be 0.
# If it terminated via sys.exit() with an integer argument N, the exit code will be N.

# If the child terminated due to an exception not caught within run(), the exit code will be 1. 
#If it was terminated by signal N, the exit code will be the negative value -N.

# Transferring error to parent
    errors = Queue()
    process = Process(target=worker2, args=(errors,))
    print("AuthKey",type(process.authkey))
    process.start()
    process.join()

    if not errors.empty():
        print("Child failed:")
        print(errors.get())

    print("Exit code:", process.exitcode)