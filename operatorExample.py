import operator
from operator import *
from numbers import *

class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

bag1 = Bag(["Book", "Pen"])
bag2 = Bag([])

print(operator.truth(bag1))
print(operator.truth(bag2))

class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

bag1 = Bag(["Book", "Pen"])
bag2 = Bag([])

print(operator.truth(bag1))
print(operator.truth(bag2))

a = [1,2,3,6,4,5]
b = a
c = [2,1,3,6,4,5]
d = None
print("is_ example below this")
print(is_(a,b))
print(is_(b,c))

print("is_not example below this")
print(is_not(a,b))
print("None example below this")
print(is_none(d))

# List of Mathematical operators available


import operator

class Temperature:
    def __init__(self, value):
        self.value = value

    def __abs__(self):
        return abs(self.value)

t = Temperature(-25)

print(operator.abs(t))
print(operator.__abs__(t))

import operator

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __repr__(self):
        return f"Money({self.amount})"

    def __radd__(self, amount):
        if isinstance(amount,Integral):
            return int(self.amount) + amount

m1 = Money(100)
m2 = Money(200)

print(operator.add(m1, m2))
print(operator.add(2,m2))

#Read this 
#operator.floordiv(a, b)
# operator.__floordiv__(a, b)
# Return a // b.
# operator.index(a)
# Return index of a

class Position:
    def __init__(self, pos):
        self.pos = pos

    def __index__(self):
        return self.pos

numbers = [10, 20, 30, 40, 50]

p = Position(2)

print(numbers[p])


#Example of invert 
import operator

class Bits:

    def __init__(self, value):
        self.value = value

    def __invert__(self):
        print("__invert__ called")
        return Bits(~self.value)

    def __repr__(self):
        return f"Bits({self.value})"

b = Bits(10)

print(operator.invert(b))
print(operator.__invert__(b))

# operator.mod(a, b)¶
# operator.__mod__(a, b)
# Return a % b.

# operator.mul(a, b)
# operator.__mul__(a, b)

print(operator.lshift(3, 4))

#Mat MUl import operator a @b

class Vector:
    def __init__(self, x):
        self.x = x

    def __matmul__(self, other):
        return self.x * other.x

v1 = Vector(6)
v2 = Vector(7)

print(operator.matmul(v1, v2))
print(v1 @ v2) #@ operator is widely used in AI


#These are also present in operators
# operator.neg(obj)
# operator.__neg__(obj)
# Return obj negated (-obj).

# operator.or_(a, b)
# operator.__or__(a, b)
# Return a | b.

#Remember to read about them as well

# operator.pow(a, b)
# operator.__pow__(a, b)
# Return a ** b.

# operator.rshift(a, b)
# operator.__rshift__(a, b)
# Return a >> b.

# operator.sub(a, b)
# operator.__sub__(a, b)
# Return a - b.

# operator.truediv(a, b)
# operator.__truediv__(a, b)
# Return a / b where 2/3 is .66 rather than 0. This is also known as “true” division.

# operator.xor(a, b)
# operator.__xor__(a, b)
# Return a ^ b.

class Temperature:
    def __init__(self, value):
        self.value = value

    def __pos__(self):
        print("__pos__ called")
        return Temperature(abs(self.value))

    def __repr__(self):
        return f"Temperature({self.value})"

t = Temperature(-25)

print(operator.pos(t))


intValues = [10, 20, 30, 40,20,30,40,20]

print(operator.contains(intValues, 20))
print(operator.contains(intValues, 50))

student = {
    "name": "Rahul",
    "age": 25
}

print(operator.contains(student, "name"))
print(operator.contains(student, "marks"))


class Basket:

    def __init__(self):
        self.items = ["Apple", "Banana", "Orange"]

    def __contains__(self, item):
        print("__contains__ called")
        return item in self.items

basket = Basket()

print(operator.contains(basket, "Banana"))

print(operator.countOf(intValues,20))

#Self exaplanatory read about them
# operator.delitem(a, b)
# operator.__delitem__(a, b)
# Remove the value of a at index b.

# operator.getitem(a, b)
# operator.__getitem__(a, b)
# Return the value of a at index b.

# operator.indexOf(a, b)
# Return the index of the first of occurrence of b in a.


# operator.setitem(a, b, c)
# operator.__setitem__(a, b, c)
# Set the value of a at index b to c.

print("Length_hint")
numbers = iter([10, 20, 30, 40])

print(operator.length_hint(numbers))

next(numbers)

print(operator.length_hint(numbers))

# Actual use of length hint
numbers = iter([10, 20, 30, 40, 50])

size = operator.length_hint(numbers)

print("Estimated size:", size)

result = [None] * size

i = 0
for value in numbers:
    result[i] = value
    i += 1

print(result)

#Example of call
class Calculator:

    def __call__(self, a, b):
        print("__call__ executed")
        return a + b

calc = Calculator()

print(operator.call(calc, 5, 7))


class GPT:

    def __call__(self, text):
        return text.upper()

class Gemini:

    def __call__(self, text):
        return text.lower()
models = [GPT(), Gemini()]

for model in models:
    print(operator.call(model, "Hello"))


#Example of attrGetter
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Rahul", 95)

get_name = attrgetter("name")

print(get_name(s))

#Another example 
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"{self.name}({self.marks})"

students = [
    Student("Rahul", 90),
    Student("Amit", 70),
    Student("Neha", 95)
]

students.sort(key=attrgetter("marks"))

print(students)

#Example of itenGetter
numbers = [10, 20, 30, 40, 50]

get_third = itemgetter(2)

print(get_third(numbers))

#FOr multiple items
numbers = [10, 20, 30, 40, 50,60]
getter = itemgetter(2, 5, 3)

print(getter(numbers))

#For tuple 
t = (100, 200, 300, 400)

getter = itemgetter(1)

print(getter(t))


#For Dictionaries
student = {
    "name": "Rahul",
    "marks": 95,
    "city": "Mumbai"
}

get_name = itemgetter("name")

print(get_name(student))

# Many operations have an “in-place” version. Listed below are functions providing a more primitive access to in-place
#  operators than the usual syntax does; for example, the statement x += y is equivalent to x = operator.iadd(x, y). 
# Another way to put it is to say that z = operator.iadd(x, y) is equivalent to the compound statement z = x; z += y.
a = 'hello'
iadd(a, ' world')

print(a)