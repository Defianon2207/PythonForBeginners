import threading
import time

#Creating a thread by subclassing thread

class DownloadThread(threading.Thread):
    def __init__(self, filename):
        # Call Thread.__init__ first
        super().__init__(name="Downloader")

        self.filename = filename

    def run(self):
        print(f"Downloading {self.filename}")
        time.sleep(2)
        print(f"Finished {self.filename}")


thread = DownloadThread("video.mp4")

thread.start()
thread.join()

#Checking if thread is alive 

def worker():
    time.sleep(2)


thread = threading.Thread(target=worker)

print(thread.is_alive())  # False

thread.start()

print(thread.is_alive())  # Usually True

thread.join()

print(thread.is_alive())  # False


#Revise subclassing

class SubclassExampleOfThread(threading.Thread):
    def __init__(self,param):
        super().__init__(name="Downloader")
        self.param = param

    def run(self):
        print(f"Console {self.param}")
        time.sleep(2)
        print(f"Finish Console {self.param}")


thread = SubclassExampleOfThread("Hey Siri")
thread.start()
print(thread.is_alive(), threading.current_thread())
thread.join()


#Custom exceptHook()

def handle_except_hook(args):
    print(f"Custom Exception, {args.thread.name}, failed : {args.exc_value}")

threading.excepthook = handle_except_hook

def worker():
    raise ValueError("Invalid Payment ammount")

thread = threading.Thread(
    target = worker,
    name ="Except_worker"
)

thread.start()
thread.join()

#Daemon Thread

stop_event = threading.Event()

def background_worker():
    while not stop_event.is_set():
        print("Background work in progress")
        time.sleep(1)
    print("Exiting gracefully")

thread = threading.Thread(
    target = background_worker,
    name = "backgorund_worker",
    daemon = False
)

thread.start()
time.sleep(3)

print("Requesting shutdown")
stop_event.set()

thread.join()

print("Program finished")