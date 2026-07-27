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