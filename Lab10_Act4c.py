# Name: Josh Stafford
# Assignment: Lab 10 Activity 4c
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.figure(figsize=(9, 9))
# Open the file
weatherData = open("WeatherDataWindows.csv")
# Set up lists to store coordinates
avgTemp = []
avgDew = []
day = 0
# Read through each line of the file
for lines in weatherData:
    # Do not do anything with the header
    if day != 0:
        # Turns each row into a list of values
        rowList = lines.split(",")
        # Store avg temp and dew point
        avgTemp.append(float(rowList[2]))
        avgDew.append(float(rowList[5]))
    # Increment the row variable
    day += 1
# Close the file
weatherData.close()
# Create the scatter plot and label the axis
plt.scatter(avgDew, avgTemp)
plt.suptitle('Average Temperature vs. Dew Point')
plt.xlabel('Dew Point')
plt.ylabel('Temperature')

plt.show()