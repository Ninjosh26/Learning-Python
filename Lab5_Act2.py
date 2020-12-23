# Name: Josh Stafford
# Assignment: Lab 5 Activity 2
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Prints the goal of the program
print("This program is designed to approximate the digits of pi")

counter = 0
for i in range(15):
    if i == 0:
        pi = 3
    elif i%2 == 1:
        pi = pi + 4 / (counter * (counter + 1) * (counter + 2))
    else:
        pi = pi - 4 / (counter * (counter + 1) * (counter + 2))
    print(pi)
    counter += 2