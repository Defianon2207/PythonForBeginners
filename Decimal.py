from decimal import *
# Set the precission to get the value of your order
getcontext().prec = 6
print(Decimal(1) / Decimal(7))

a = Decimal(57.50)
b = Decimal(105.67)
print(a+ b)
print(Decimal(3.14))
print(Decimal('-Infinity'))
print(Decimal("3.14"))
print(Decimal((0, (3,1,4), -2)))

# getcontext().traps[FloatOperation] = True

# print("Trapped after setting true",Decimal(3.14))

data = list(map(Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
print(data)
max(data)
print(sorted(data))

#Adjusted 
print(Decimal('321e+5').adjusted())
print(Decimal('-3.14').as_integer_ratio())
print(DecimalTuple(sign, digits, exponent))