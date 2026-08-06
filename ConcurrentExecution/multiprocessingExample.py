from multiprocessing import Pool, Process


def f(x):
    return x*x

def fpro(name):
    print(f"Name is : {name}")

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

    p = Process(target =fpro, args=("Defianon",))
    p.start()
    p.join()