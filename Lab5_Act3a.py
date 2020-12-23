# Name: Josh Stafford
# Assignment: Lab 5 Activity 3a
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Prints the goal of the program
print("This program is designed to print the Collatz sequence")
# Asks the user for a starting positive integer
num = int(input("Please enter a positive integer"))
counter = 0
print(num, end = " ")
while(not num == 1):
    if num%2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1
    print(num, end = " ")
    counter += 1
print("The sequence took", counter, "loops")
