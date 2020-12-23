# Name: Josh Stafford
# Assignment: Lab 4 Activity 7
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
from math import *
# Asks the user to input the coefficients of the quadratic equation
a = float(input("Please enter the coefficient A:"))
b = float(input("Please enter the coefficient B:"))
c = float(input("Please enter the coefficient C:"))
# Checks to see what method will be used to find the roots
if a == 0:
    if b == 0:
        if c == 0:
            print("c is correctly 0, and there are no roots")
        else:
            print("Incorrect, c should be 0")
    else:
        print("The only root is", -c / b)
else:
    radical = b**2 - 4 * a * c
    if radical < 0:
        radical = str(sqrt(-radical) / (2 * a)) +"i"
        print("The roots are", b / (2 * a), "+", radical, "and",  b / (2 * a), "-", radical)
    else:
        radical = sqrt(radical)
        print("The roots are", (b + radical) / (2 * a),"and",  (b - radical) / (2 * a))