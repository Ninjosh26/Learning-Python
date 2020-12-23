# Name: Josh Stafford
# Assignment: Lab 3 Activity 3a
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

from math import*

# (a) Ohm's Law: Calculate the voltage across a conductor
print("This program calculates voltage given resistance and current")
# Asks user for input
resistance = input("Please enter the resistance of the conductor (ohms): ")
current = input("Please enter the current of the conductor (amperes): ")
voltage = float(resistance) * float(current)
# Prints calculated value
print("The voltage is", voltage, "V")