# Name: Josh Stafford
# Assignment: Lab 3 Activity 1d
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

print("This program converts Seconds per revolution to Hertz")
# Asks user to input Seconds per revolution
secPerRev = input("Please enter the Seconds per revolution to be converted to Hertz:")
# Converts Seconds per revolution to Hertz
hertz = 1 / (float(secPerRev))
print(secPerRev, "Seconds per revolution is equivalent to", hertz, "hertz")