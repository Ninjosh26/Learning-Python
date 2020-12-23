# Name: Josh Stafford
# Assignment: Lab 5 Activity 3b
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Prints the goal of the program
print("This program is designed to print the sum and product of all numbers up to given number")
# Asks the user for a ending positive integer
num = int(input("Please enter a positive integer"))
sum = 0
product = 1
# Sum with a for loop
for i in range(num + 1):
    sum += i
print("The sum of all numbers up to", num, "is", sum)
# Sum with a while loop
count = 0
sum = 0
while(count <= num):
    sum += count
    count += 1
print("The sum of all numbers up to", num, "is", sum)
# Product with a for loop
for i in range(num):
    product *= i + 1
print("The product of all numbers up to", num, "is", product)
# Product with a while loop
count = 1
product = 1
while(count <= num):
    product *= count
    count += 1
print("The product of all numbers up to", num, "is", product)