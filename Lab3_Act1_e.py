# Name: Josh Stafford
# Assignment: Lab 3 Activity 1e
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

print("This program converts from Miles per Hour to Meters per Second")
# Asks user to input Miles per Hour
mph = input("Please enter the Miles per Hour to be converted to Meters per Second:")
# Converts Seconds per revolution to Hertz
mps = float(mph) * 1609.34 / 3600
print(mph, "Miles per Hour is equivalent to", mps, "Meters per Second")