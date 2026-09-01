from multiprocessing import Manager


if __name__ == "__main__":
    with Manager() as manager:
        shared_list = manager.list([1, 2, 3])
        shared_dict = manager.dict({"status": "pending"})
        shared_set = manager.set({"python", "rust"})

        print(list(shared_list))
        print(dict(shared_dict))
        print(set(shared_set))