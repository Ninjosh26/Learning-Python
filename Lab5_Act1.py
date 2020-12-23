# Name: Josh Stafford
# Assignment: Lab 5 Activity 1
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Test cases used were:
# x^3+2x^2-x-2
# 2x^3+x^2-13x+6
# 6x^3+34x^2+18x-10
# -6x^3+7x^2+29x+12

# Prints the gaol of the program
print("The program is designed to find a root of a cubic function.")
# Asks the user to come up with coefficients for the cubic function
a = float(input("Please enter the coefficient, A"))
b = float(input("Please enter the coefficient, B"))
c = float(input("Please enter the coefficient, C"))
d = float(input("Please enter the coefficient, D"))
# Sets the bounds a and b
boundA = float(input("Please enter the lower bound, A"))
boundB = float(input("Please enter the upper bound, B"))
# Create a counting variable
count = 1


# Creates a function to compute values of f(x)
def compute(x):
    return (a * x ** 3) + (b * x ** 2) + (c * x) + d


# Attempts to find a root within a tolerance of 10^-6
while abs((boundB - boundA)) > 0.000001:
    # Bisects the interval
    p = (boundB - boundA) / 2 + boundA
    # Evaluates if the interval is decreasing
    if compute(boundA) > compute(boundB):
        # Picks which half to use
        if compute(p) > 0:
            boundA = p
        elif compute(p) < 0:
            boundB = p
        else:
            # Ends the loop if the zero is at the bisection
            zero = p
            break
    # Evaluates if the interval is increasing
    if compute(boundA) < compute(boundB):
        # Picks which half to use
        if compute(p) > 0:
            boundB = p
        elif compute(p) < 0:
            boundA = p
        else:
            # Ends the loop if the zero is at the bisection
            zero = p
            break
    count += 1
    zero = boundA
# Prints the calculated root
print("A zero of the cubic function is", zero)
# Prints the amount of loops executed
print("This calculation took", count, "loops")
