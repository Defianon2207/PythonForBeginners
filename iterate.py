from itertools import *

numbers = list(map(int,"1 2 13 4 5".split()))
print(numbers)
result = list(accumulate(numbers))
result2 = list(accumulate(numbers, max))
print(result,result2)

internt_status = ["highSpeed", "Low Speed", "medium speed", "ultra high", "suspended", "blocked"]

for batch in batched(internt_status,2):
    print(batch)

from itertools import batched


# You can use batched to send bulk API request - Try this example when you have enough Idea about it

def numbers():
    for i in range(10):
        yield i

for batch in batched(numbers(), 4):
    print(batch)

# Example of chain how it works

for x in chain(internt_status, result, result2):
    print("chain",x)

# Example of how comb works
for comb in combinations(internt_status, 2):
        print(comb)

