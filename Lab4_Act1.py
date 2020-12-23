# Name: Josh Stafford
# Assignment: Lab 4 Activity 1
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# define tolerance
TOL = 1e-10

# Part 1a
a = 1 / 7
print(a)
b = a * 7
print(b)
print("")

a = 1 / 7
print(a)
b = 7 * a
print(b)
c = 2 * a
d = 5 * a
e = c + d
print(e)
# check if b and e are equal within specified tolerance
if abs(b-e) < TOL:
    print("b and e are equal within tolerance of", TOL)
else:
    print("b and e are NOT equal within tolerance of",TOL)
print("")

from math import *

x = sqrt(1 / 3)
print(x)
y = x * x * 3
print(y)
z = x * 3 * x
print(z)
# check if b and e are equal within specified tolerance
if abs(y-z) < TOL:
    print("y and z are equal within tolerance of", TOL)
else:
    print("y and z are NOT equal within tolerance of",TOL)
print("")

# Part 1b
# Subtracting using integers
x = 1234567891234567
y = 1234567891234566
z = x**2 - y**2
print(z)

# Subtracting using floating points
x = 1234567891234567.0
y = 1234567891234566.0
z = x**2 - y**2
print(z)

# Subtracting using (x+y)(x-y)
x = 1234567891234567.0
y = 1234567891234566.0
z = (x+y)*(x-y)
print(z)
