# Given an array of integers and a number k, find the maximum sum of any k consecutive elements.

# numbers = [2, 1, 5, 1, 3, 2]
# k = 3

# 1) How many combinations can ne their of 3 consicutive number.

import math 

print(math.comb(6,1))

numbers = [2, 1, 5, 1, 3, 2]
k = 3
sum=[]

#Generate sum of all combinations possible
i = 0
while i < len(numbers):
    j = 0
    m = numbers[:i] + numbers[i+1:]
    while j < len(m)-1:
        #Some logic
        z=0
        o = m[:j] + m[j+1:]
        while z < len(o)-1:
            sum.append(numbers[i] + m[j] + o[z])
            z=z+1
        j =j+1
    i = i + 1

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

