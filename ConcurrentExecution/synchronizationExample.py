from multiprocessing import Process, Lock
import time

def worker(lock, number):
    with lock:
        print(f"Process {number}: starting")
        time.sleep(1)
        print(f"Process {number}: finishing")

if __name__ == "__main__":
    lock = Lock()
    processes = []

    for number in range(20):
        process = Process(target=worker, args=(lock, number))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


# from multiprocessing import Process, Lock
# import time

# def write_log(lock, process_number):
#     with lock:
#         with open("activity.log", "a") as file:
#             file.write(f"Process {process_number} started writing\n")
#             time.sleep(0.5)
#             file.write(f"Process {process_number} finished writing\n")

# if __name__ == "__main__":
#     lock = Lock()
#     processes = []

#     for number in range(5):
#         process = Process(
#             target=write_log,
#             args=(lock, number)
#         )
#         process.start()
#         processes.append(process)

#     for process in processes:
#         process.join()