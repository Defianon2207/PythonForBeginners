import threading
import time


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