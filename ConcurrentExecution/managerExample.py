from multiprocessing import Process, Manager


def f(d, l, s):
    d[1] = "1"
    d["2"] = 2
    d[0.25] = None

    l.reverse()

    s.add("a")
    s.add("b")


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