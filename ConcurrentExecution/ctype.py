from multiprocessing import Process, Value, Array


# def increment_counter(counter):
#     for _ in range(10_000):
#         with counter.get_lock():
#             counter.value += 1


# if __name__ == "__main__":
#     # "i" means signed integer, initially set to 0
#     counter = Value("i", 0)

#     processes = []

#     for _ in range(4):
#         process = Process(
#             target=increment_counter,
#             args=(counter,)
#         )
#         process.start()
#         processes.append(process)

#     for process in processes:
#         process.join()

#     print("Final counter:", counter.value)

# def change_number(shared_number):
#     print("Child received:", shared_number.value)

#     shared_number.value = 100

#     print("Child changed it to:", shared_number.value)


# if __name__ == "__main__":
#     number = Value("i", 10)

#     process = Process(
#         target=change_number,
#         args=(number,)
#     )

#     process.start()
#     process.join()

#     print("Parent sees:", number.value)
def update_number(num):
    print("Number received :",num.value)
    for _ in range(100_000):
        with num.get_lock():
            num.value = num.value + 1

def square_function(arr):

    for index in  range(len(arr)):
        arr[index] = arr[index] ** arr[index]


if __name__ == "__main__":
    number = Value("i", 0)

    processes = [Process(target = update_number,args = (number,))
    for _ in range(4)
    ]

    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
        
    print("Number after update", number.value)

    array = Array("i", [1,2,3,4,5,6])

    p = Process(
        target = square_function,
        args = (array,)
    )
    p.start()
    p.join()
    print("Final Array", list(array))