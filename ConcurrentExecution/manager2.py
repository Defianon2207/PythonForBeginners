from multiprocessing import Process, Manager


def add_user(users, user_id, name):
    users[user_id] = name

def calculate_square(number, results):
    results.append(number ** 2)


if __name__ == "__main__":
    with Manager() as manager:
        users = manager.dict()

        processes = [
            Process(target=add_user, args=(users, 1, "Rahul")),
            Process(target=add_user, args=(users, 2, "Aman")),
            Process(target=add_user, args=(users, 3, "Priya")),
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        print(dict(users))
    with Manager() as manager:
        results = manager.list()

        processes = [
            Process(
                target=calculate_square,
                args=(number, results)
            )
            for number in range(1, 6)
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        print(list(results))