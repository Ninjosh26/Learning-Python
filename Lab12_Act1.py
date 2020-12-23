# Name: Josh Stafford
# Assignment: Lab 12 Activity 1
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
import math

# Part A: Find the remaining volume of a box with a hole in it


def volumeRemain(length, width, height, radius):
    """ Takes a length, width, height, and radius value, and returns an int or float. The function determines
    the remaining volume of a box with length, width, and height, after a hole with radius has been drilled
    through it"""
    # if the hole is within the box
    if min(length / 2, width / 2) >= radius:
        volumeBox = length * width * height
        volumeCyl = math.pi * radius ** 2 * height
        # Difference in the volumes of the cube and cylinder
        return volumeBox - volumeCyl


print(volumeRemain(4, 4, 4, 2), "\n")

# Part B: Find the least profitable factory


def netProfit(names, costs, values):
    """ Takes a list of names, costs, and product values of lists, and returns a string. The lists must be
    parallel, with each element corresponding to each other. Determines the least profitable factory by
    finding the factory with lowest net profit, determined by subtracting the costs from the profit values."""
    profit = []
    # Find the profit of each factory
    for i in range(len(names)):
        profit.append(values[i] - costs[i])
    low = profit.index(min(profit))
    # Return the least profitable factory
    return "The least profitable factory is " + str(names[low]) + " with a net profitability of " + str(profit[low])


# Part C: Create a mailing label


def mailLabel(name, city, state, zipCode, address, address2=""):
    """ Takes a name, city, state, zip code, address, and address 2 (optional), and returns a string. The
     function creates a mailing label using certain parts of a physical address and information."""
    # Create mail address with only one address
    if address2 == "":
        return str(name) + "\n" + str(address) + "\n" + str(city) + ", " + str(state) + " " + str(zipCode)
    # Create mail address with 2 addresses
    else:
        return str(name) + "\n" + str(address) + "\n" + str(address2) + "\n" + str(city) + ", " \
               + str(state) + " " + str(zipCode)


# Part D: Change a csv file to a tsv


def fileChange(csv, tsv):
    """ Takes in 2 strings and has no returns. The function takes the name of a csv file, and writes its
    data into a desired tsv file."""
    # Open both files
    fileA = open(csv, "r")
    fileB = open(tsv, "w")
    # Take each line in the csv
    for i in fileA:
        # Put every value in a list without the commas
        temp = i.split(",")
        i = 1
        # Insert tabs between each value
        while i < len(temp):
            temp.insert(i, '\t')
            i += 2
        # Write the values into the new file
        for j in temp:
            fileB.write(str(j))


# Part E: Find the min, max, and mean value of a list


def average(list):
    """ Takes a list and returns an int or float. Function takes a list of values, and returns its average."""
    return sum(list) / len(list)


def listStuff(list):
    """ Takes a list and returns a string. The function finds the minimum, maximum, and average values in
    a given list, and returns them as a string."""
    return "The min is " + str(min(list)) + ", the max is " + str(max(list)) + ", the mean is " + str(average(list))


# Part F: Create a list of the average velocity


def avgVel(times, distance):
    """ Takes in 2 lists, and returns a list. The function takes a list of times and list of distances,
    then creates a list of the average velocities."""
    # Creates an empty list
    avgVelocity = []
    # Finds the velocity for each time interval, then appends it to the list of velocities
    for i in range(len(times) - 1):
        velocity = (distance[i + 1] - distance[i]) / (times[i + 1] - times[i])
        avgVelocity.append(velocity)
    # Returns a list of average velocities
    return avgVelocity
