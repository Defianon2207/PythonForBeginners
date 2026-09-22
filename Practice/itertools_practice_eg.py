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