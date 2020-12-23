# Name: Josh Stafford
# Assignment: Lab 6 Activity 4
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

from math import *

a = []
b = []
# Asks the user for the dimensions of the vectors
dimension = int(input("How many dimensions do the vectors have?:"))
# Asks for the first element in the first vector
a.append(int(input("Please enter the first element of the first vector:")))
# Adds more elements if needed
for i in range(dimension - 1):
    a.append(int(input("Please enter the next element:")))
# Asks for the first element in the second vector
b.append(int(input("Please enter the first element of the second vector:")))
# Adds more elements if needed
for j in range(dimension - 1):
    b.append(int(input("Please enter the next element:")))


# Finds the magnitude of a vector
def magnitude(x):
    mag = 0
    for k in x:
        mag += k ** 2
    return sqrt(mag)


# Adds the vectors
def addition(x, y):
    add = []
    for l in range(len(x)):
        add.append(x[l] + y[l])
    return add


# Subtracts the vectors
def subtraction(x, y):
    sub = []
    for m in range(len(x)):
        sub.append(x[m] - y[m])
    return sub


# Calculates the dot product of two vectors
def dotProduct(x, y):
    dot = 0
    for n in range(len(x)):
        dot += x[n] * y[n]
    return dot


# Prints the maintude of the vectors
print("The magnitude of A is:", magnitude(a))
print("The magnitude of B is:", magnitude(b))
# Prints the added vectors
print("Adding A and B results in:", addition(a, b))
# Prints the subtracted vectors
print("Subtracting A and B results in:", subtraction(a, b))
# Prints the dot product of the vectors
print("The dot product of A and B is:", dotProduct(a, b))
