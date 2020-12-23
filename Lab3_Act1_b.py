# Name: Josh Stafford
# Assignment: Lab 3 Activity 1b
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

print("This program converts BTUs to Joules")
# Asks user to input BTUs
btu = input("Please enter the number of BTUs to be converted to Joules:")
# Converts BTUs to Joules
joules = float(btu) * 1055.05585
print(btu, "BTUs is equivalent to", joules, "Joules")