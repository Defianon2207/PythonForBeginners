from itertools import *

numbers = "1 12 13 12 52"
print(list(accumulate(map(int,numbers.split()))))

#Whenever their is string in the python
number =[]
for i in range(9):
    number.append(i)

print(list(accumulate(number)))