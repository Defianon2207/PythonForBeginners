# Given an array of integers and a number k, find the maximum sum of any k consecutive elements.

# numbers = [2, 1, 5, 1, 3, 2]
# k = 3

# 1) How many combinations can ne their of 3 consicutive number.

import math 

print(math.comb(6,1))

numbers = [2, 1, 5, 1, 3, 2]
k = 3
sum=[]
combination_sums = []

i = 0

while i < len(numbers) - 2:
    j = i + 1

    while j < len(numbers) - 1:
        z = j + 1

        while z < len(numbers):
            combination = [
                numbers[i],
                numbers[j],
                numbers[z]
            ]

            combination_sum = (
                numbers[i] +
                numbers[j] +
                numbers[z]
            )

            print(combination, "→", combination_sum)
            combination_sums.append(combination_sum)

            z += 1

        j += 1

    i += 1

print("Combination sums:", combination_sums)
print("Generated combinations:", len(combination_sums))
print("Expected combinations:", math.comb(len(numbers), k))

# print(sum,len(sum))

#Circular Sliding Window problem

slidingSum =[]
t = 0
while t < len(numbers):
    j = t+1
    if( j > len(numbers) - 1 ):
        j = j - len(numbers) 
    l = t+2
    if( l > len(numbers)-1 ):
        l = l - len(numbers) 
        print(t,)
    slidingSum.append(numbers[t] + numbers[j] + numbers[l])
    t =t+1

print(slidingSum)

