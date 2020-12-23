# Name: Josh Stafford
# Assignment: Lab 7 Part 2
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Prints goal of program
print("This program returns a value of stress for a given strain input")
# Establish starting slope values as variables
slopeOne = 3520
slopeThree = 16 / 0.12
slopeFour = - 8 / 0.0825
# Ask the user to input a value of strain for which they would like to find stress.
inputStrain = float(input("Please enter a strain point from 0 to 0.2625:"))
# If the strain is past or below the boundaries, print an error statement and ends program
if inputStrain > 0.2625 or inputStrain < 0:
    print("That is not a valid strain value")
    quit()
# If the strain is on the 4th segment, use the 4th slope to interpolate
elif inputStrain > 0.18:
    outputStress = slopeFour * (inputStrain - 0.18) + 60
# If the strain is on the 3rd segment, use the 3rd slope to interpolate
elif inputStrain > 0.06:
    outputStress = slopeThree * (inputStrain - 0.06) + 44
# If the strain is on the 2nd segment, use the 2nd slope to interpolate
elif inputStrain > 0.0125:
    outputStress = 44
# If the strain is on the 1st segment, use the 1st slope to interpolate
else:
    outputStress = slopeOne * inputStrain
# Print the value of stress
print("The stress at a strain of", inputStrain, "is", outputStress)
