from multiprocessing.managers import BaseManager

class Counter:
    def __init__(self):
        self._value = 0

    def increment(self):
        self._value += 1
    
    def get_value(self):
        return self._value


class MyManager(BaseManager):
    pass

MyManager.register("Counter", Counter)


if __name__ == "__main__":
    manager = MyManager()
    manager.start() # This can be skipped if you use with Mymanager as manager this will eliminated the above 2 lines

    counter = manager.Counter()

    counter.increment()
    counter.increment()

    print(counter.get_value())  # 2

    manager.shutdown()
