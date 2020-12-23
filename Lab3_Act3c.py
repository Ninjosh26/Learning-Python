# Name: Josh Stafford
# Assignment: Lab 3 Activity 3b
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

from math import *

# (c) Mohr-Coulomb Failure Criterion: calculate the shear stress
print("This program calculates shear stress given normal stress, cohesion, and the angle of internal friction")
# Asks user for input
nStress = input("Please enter the normal stress (lbf/in^2): ")
cohesion = input("Please enter the cohesion (lbf/in^2): ")
angle = input("Please enter the angle of internal friction(degrees): ")
mohrCoulomb = float(nStress)*tan(radians(float(angle))) + float(cohesion)
# Prints calculated value
print("The shear stress is", mohrCoulomb, "lbf/in^2")