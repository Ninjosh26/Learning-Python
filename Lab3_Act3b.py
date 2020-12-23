# Name: Josh Stafford
# Assignment: Lab 3 Activity 3b
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

from math import *

# (b) Kinetic Energy: Calculate the kinetic energy of an object
print("This program calculates kinetic energy given mass and velocity")
# Asks user for input
mass = input("Please enter the mass of the object(kg): ")
velocity = input("Please enter the velocity of the object(mps): ")
kinetic = 1 / 2 * float(mass) * pow(float(velocity), 2)
# Prints calculated value
print("The kinetic energy is", kinetic, "J")
