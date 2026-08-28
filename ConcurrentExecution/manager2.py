from multiprocessing import Process, Manager


def add_user(users, user_id, name):
    users[user_id] = name


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