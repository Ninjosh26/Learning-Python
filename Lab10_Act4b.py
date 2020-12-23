# Name: Josh Stafford
# Assignment: Lab 10 Activity 4b
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.figure(figsize=(9, 9))
# Open the file
weatherData = open("WeatherDataWindows.csv")
# Set up lists to store coordinates
precipitation = []
day = 0
# Read through each line of the file
for lines in weatherData:
    # Do not do anything with the header
    if day != 0:
        # Turns each row into a list of values
        rowList = lines.split(",")
        # Store the precipitation
        precipitation.append(float(rowList[-1]))
    # Increment the row variable
    day += 1
# Close the file
weatherData.close()
# Create the histogram and label the axis
plt.hist(precipitation, 50)
plt.suptitle('Precipitation')
plt.xlabel('Inches of rain')
plt.ylabel('Amount of days')

plt.show()