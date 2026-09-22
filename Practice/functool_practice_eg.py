from functools import *
import statistics

# @cache
# def fibonacci(n):
#     print(f"Calculating fib({n})")

#     if n < 2:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(3))


@cache
def factorial(n):
    if n > 1:
       return n * factorial(n-1)
    else: 
        return 1

factorial_5 = factorial(5)
print(factorial_5, factorial(6), factorial(20))
print(factorial.cache_info())


class DataSet:

    def __init__(self, sequence_of_numbers):
        self._data = tuple(sequence_of_numbers)

    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)
n = [12,34,23,43,52,56]
p =  DataSet(n)
print(p._data, p.stdev)
print(p.stdev)

@lru_cache
def count_vowels(sentence):
    return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')

print(count_vowels("sfjewurhndjhhdhdaaaaaa"))