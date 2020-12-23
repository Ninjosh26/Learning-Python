# Name: Josh Stafford
# Assignment: Lab 6 Activity 5
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# (a) Write a program to multiply all the items of a list (you can assume they are all numbers)
# Establishes a list
a = [1, 2, 3, 4]
num = 1
# Loops through and multiplies all the values of the list
for i in a:
    num *= i
print(num)

# (b) Write a program to find the largest number in a list
b = [23, 18, 5, 68, 3, 56, 2]
temp = b[0]
for j in b:
    if i > temp:
        temp = i
print(temp)

# (c) Write a program to find the second smallest number in a list
c = [5, 3, 76, 8, 7, 54, 6, 24, 12]
# Sorts c in increasing order
c.sort()
print(c[1])

# (d) Write a program to get a list which is sorted by the last element of each member list
d = [[2, 6, 3], [8, 2, 6], [7, 2, 9], [5, 3, 7]]
# Sorts the list of list, using the the last element of each sublist as a basis for comparisons
print(sorted(d, key=lambda lists: lists[-1]))

# (e) Write a program which removes all duplicates from a list
e = [2, 6, 4, 8, 90, 23, 6, 34, 65, 1, 4, 45, 5, 2]
noDupes = []
# Loops through e and add an element to noDupes if it is not already there
for k in e:
    if k not in noDupes:
        noDupes.append(k)
e = noDupes
print(e)
