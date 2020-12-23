# Name: Josh Stafford
# Assignment: Lab 3 Activity 3b
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

from math import *

# (d) Arps equation: calculate the production of a well
print("This program calculates production of a well given days, production rate, decline rate, and hyperbolic constant")
# Asks user for input
time = input("Please enter the time in days: ")
productRate = input("Please enter the production rate in barrels per day: ")
decRate = input("Please enter the decline rate in barrels per day: ")
hypbolicC = input("Please enter the hyperbolic constant: ")
arps = float(productRate)/(pow(1 + float(hypbolicC)*float(decRate)*float(time), 1/float(hypbolicC)))
# Prints calculated value
print("The production of the well is", arps, "barrels per day")