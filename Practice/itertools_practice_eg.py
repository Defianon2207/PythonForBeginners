from itertools import *

numbers = "1 12 13 12 52"
print(list(accumulate(map(int,numbers.split()))))

#Whenever their is string in the python
number =[]
for i in range(9):
    number.append(i)

print(list(accumulate(number)))

#Workiing with batched data

unbatched = ["Rahul", "Namit", "Rachit", "Sachit", 
"Neymar", "Messi","Ritesh","Rakesh", "NONONO"]

batched_data = list(batched(unbatched,2,strict = False)) # False is a important parameter in the python
print(batched_data)

for k in batched_data:
    print("Batch re Batch ",k)


#Examples of chain
internt_status = ["highSpeed", "Low Speed", "medium speed", "ultra high", "suspended", "blocked"]
Data = ["ABCD", "DEFGH", "JKLMN"]

for x in chain(internt_status, Data):
    print(x)

#Example of combination
combinations_result = list(combinations(internt_status,2))
print("Total Combination",len(combinations_result))

#Example of Yield
#Yield holds the value in the 
def numbers_yield():
    for i in range(10):
        yield i

counter = numbers_yield()
for i in range(10):
    print(next(counter))

#Example of combination_with_replacement

result = list(combinations_with_replacement(internt_status,2))
print(len(result), result, sep ="\n",end="\n")

#Example of compress 
data =["A","B","C","D","E","F","G","G","H","L","F","T"]
datum=[1,1,1,1,1,1,1,0,1,1,1,0]

print(list(compress(data,datum)))

c = cycle(internt_status)


for _ in range(1,10):
    print(next(c))



#Example of filter false

filtered_data = filterfalse(lambda x : x == "Low Speed", internt_status)
print(list(filtered_data))

#Filtered Data -- No Delta

#dropwhille example
dropped_list = dropwhile(lambda x : x != "suspended", internt_status)
print("dropList",list(dropped_list))

#Group by example 

students = [
    ("A", "Rahul"),
    ("A", "Aman"),
    ("B", "Rohit"),
    ("B", "Ajay"),
    ("C","Kedia")
]

for grade, group in groupby(students, key=lambda x: x[0]):
    print(grade, list(group))

for _ in pairwise(internt_status):
    print("pairwise")
    print(_)


# While starmap
li =[(2, 5), (3, 2), (4, 3)]

new_li = list(starmap(pow, li))
print(new_li)

#Star map example

def add(a,b):
    return a+b

sumed = list(starmap(add,li))

#Permutation repeat

take_data = takewhile(lambda x: x<5, [1,4,6,3,8])

print(list(take_data))

a,b,c=tee(internt_status,3)
print(list(a),list(b),list(c), sep="\n")