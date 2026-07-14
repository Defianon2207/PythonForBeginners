from functools import *

@cache
def fibonacci(n):
    print(f"Calculating fib({n})")

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))

class DataSet:

    def __init__(self, sequence_of_numbers):
        self._data = tuple(sequence_of_numbers)

    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)
n = [12,34,23,43,52,56]
p =  DataSet(n)
print(p._data)

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent =2)
print(square(5))