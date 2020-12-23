# Name: Josh Stafford
# Assignment: Lab 10 Activity 1
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
import numpy as np

# Creates and prints 4 arrays with different shapes: a, b, c, and d
a = np.array([1, 5, 6, 6, 7, 5, 4, 9, 7, 3, 5, 7]).reshape(3, 4)
print("a:")
print(a, "\n")
b = np.array([5, 1, 8, 3, 8, 4, 5, 7]).reshape(4, 2)
print("b:")
print(b, "\n")
c = np.array([3, 8, 6, 9, 2, 6]).reshape(2, 3)
print("c:")
print(c, "\n")
d = np.array([2, 6, 8]).reshape(3, 1)
print("d:")
print(d, "\n")

# Finds e: the dot product of a b and c
e = a @ b @ c
print("The dot product of a, b, and c:\n", e, "\n")

# Transposes e
print("The transpose of their dot product, e:\n", np.transpose(e), "\n")

# Solves ex = d
x = np.linalg.solve(e, d)
print("The solution to ex = d is:\n", x)


