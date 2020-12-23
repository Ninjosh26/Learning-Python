# Name: Josh Stafford
# Assignment: Lab 10 Activity 4a
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.figure(figsize=(9, 9))
# Open the file
weatherData = open("WeatherDataWindows.csv")
# Set up lists to store coordinates
averageTemperature = []
averagePressure = []
day = 0
dayList = []
# Read through each line of the file
for lines in weatherData:
    # Do not do anything with the header
    if day != 0:
        # Turns each row into a list of values
        rowList = lines.split(",")
        # Store the day, avg temp, and avg pressure
        dayList.append(day)
        averageTemperature.append(int(rowList[2]))
        averagePressure.append(float(rowList[11]))
    # Increment the row variable
    day += 1
# Close the file
weatherData.close()
# Create 2 plots
plt.subplot(211)
# Plot the days and temperature
temp = plt.plot(dayList, averageTemperature)
# Create the legend and labels
blue_patch = mpatches.Patch(color='blue', label='Temperature')
plt.legend(handles=[blue_patch], loc='upper left')
plt.xlabel('Day')
plt.ylabel('Temperature')

plt.subplot(212)
# Plot the days and pressure
pressure = plt.plot(dayList, averagePressure, 'g')
# Create the legend and labels
green_patch = mpatches.Patch(color='green', label='Pressure')
plt.legend(handles=[green_patch], loc='upper left')
plt.xlabel('Day')
plt.ylabel('Pressure')
plt.suptitle('Temperature and Pressure vs. Time')

plt.show()