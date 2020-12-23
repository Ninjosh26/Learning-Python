# Name: Josh Stafford
# Assignment: Lab 4 Activity 4
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Asks user to input 3 numbers
num1 = float(input("Please enter a number:"))
num2 = float(input("Please enter another number:"))
num3 = float(input("Please enter one more number:"))
# Evaluates which number is the largest and prints it
if num1 > num2 and num1 > num3:
    print(num1, "is the largest")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest")
else:
    print(num3, "is the largest")