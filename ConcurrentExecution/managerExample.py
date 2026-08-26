from multiprocessing import Process, Manager


def f(d, l, s):
    d[1] = "1"
    d["2"] = 2
    d[0.25] = None

    l.reverse()

    s.add("a")
    s.add("b")

def add_user(shared_users, user_id, name):
    shared_users[user_id] = name
    print(f"Added {name}")


if __name__ == "__main__":
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        s = manager.set()

        process = Process(target=f, args=(d, l, s))
        process.start()
        process.join()

        print(dict(d))
        print(list(l))
        print(set(s))

        with Manager() as manager:
        # A dictionary shared between processes
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

        print("Shared dictionary:", dict(users))