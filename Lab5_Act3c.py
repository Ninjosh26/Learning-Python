# Name: Josh Stafford
# Assignment: Lab 5 Activity 3c
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Prints the goal of the program
print("This program prints if the numbers between 2 and 100 are prime")
# Establish counting variable
count = 0
# Creates loop for number being tested from 2 - 100
for i in range(2, 101):
    # Establishes boolean to represent if a number is prime
    prime = True
    # Creates loop to test if a number is divisible by numbers before it
    for j in range(2, i):
        # If a number is evenly divisible, prints it is not prime and ends the loop
        if i % j == 0:
            print(i, "is not prime")
            prime = False
            break
    # If the number is prime, prints it is prime and increments counter
    if prime:
        print(i, "is prime")
        count += 1
# Prints the amount of primes
print("There are", count, "number of primes between 2 and 100")
