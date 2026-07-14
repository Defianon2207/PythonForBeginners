from itertools import *

numbers = list(map(int,"1 2 13 4 5".split()))
print(numbers)
result = list(accumulate(numbers))
result2 = list(accumulate(numbers, max))
print(result,result2)

internt_status = ["highSpeed", "Low Speed", "medium speed", "ultra high", "suspended", "blocked"]
TruthTable = [1,1,0,1,0,1]
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

#Example of how compress works

for comp in compress(internt_status,TruthTable):
    print(comp)

#Example of cycle
c = cycle(internt_status)
for _ in range(1,10):
    print(next(c))

#Example of dropped List
dropped_list = dropwhile(lambda x : x != "Low Speed", internt_status)
print(list(dropped_list))

#Exmple of Filter False --> Removes all the element for which conditon is True

false_filter_list = filterfalse(lambda x : x =="Low Speed", internt_status)
print(list(false_filter_list))

#Group by Example -
students = [
    ("A", "Rahul"),
    ("A", "Aman"),
    ("B", "Rohit"),
    ("B", "Ajay"),
]

for grade, group in groupby(students, key=lambda x: x[0]):
    print(grade, list(group))

#Eaxample of pairwise, It look simple but it can be  very useful

for _ in pairwise(internt_status):
    print(_)

# Example of starMap

li =[(2, 5), (3, 2), (4, 3)]

new_li = list(starmap(pow, li))

print(new_li)
