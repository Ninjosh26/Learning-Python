# Name: Josh Stafford
# Assignment: Lab 9 Activity 1
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Opens the file with celsius values
celsius = open("Celsius.dat", "r")
# Opens the file with fahrenheit values
fahrenheit = open("Fahrenheit.dat", "w")
# Converts each celsius value to fahrenheit, and writes it in the fahrenheit file
for line in celsius:
    f = (int(line) * 9 / 5) + 32
    fahrenheit.write(str(f) + "\n")
# Closes both files
celsius.close()
fahrenheit.close()