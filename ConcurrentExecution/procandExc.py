import os
from multiprocessing import Process

def welcome(name,greetings):
    print(os.getpid())
    print(f"{greetings}, {name}")

def worker(number):
    print("PID:", os.getpid(), os.getppid())
    print("Square:", number * number)

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