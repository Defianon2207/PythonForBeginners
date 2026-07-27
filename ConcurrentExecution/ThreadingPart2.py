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
print(mydata.squared())