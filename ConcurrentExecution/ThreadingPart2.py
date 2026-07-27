import threading
import time
from threading import local

class MyLocal(local):
    # Default value available in every thread
    number = 2

    def __init__(self, /, **kwargs):
        print("Initializing for:", threading.current_thread().name)

        # Store the supplied values in the current thread's dictionary
        self.__dict__.update(kwargs)

    def squared(self):
        return self.number ** 2


mydata = MyLocal(color="red")
# print(mydata.squared())
# print(mydata.color)
# print(mydata.number, mydata.name)
# print(mydata.__dict__)

# creating multiple threads

log =[]

def worker(color):
    mydata.color = color
    mydata.number = 11

    time.sleep(1)

    print(
        threading.current_thread().name,
        mydata.color,
        mydata.__dict__
    )

threads = [threading.Thread(target=worker,args =('red',), name="Worker1"),
threading.Thread(target=worker,args =('green',), name="Worker2"),
]

for thread in threads:
    thread.start()

for thread in threads:
      thread.join()

print("Log",log)

