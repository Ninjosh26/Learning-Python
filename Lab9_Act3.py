# Name: Josh Stafford
# Assignment: Lab 9 Activity 3
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# A value to keep track of what row the program is on
row = 1
# Sets a default max, min, precipitation, humidity, and pressure above values
maxTemp = 0
minTemp = 0
totalPrecip = 0
totalHumidityHigh = 0
pressureAbove = 0
# Asks the user to input a specific day
userDate = input("Enter a day between 1/1/2015 and 12/31/2017 (mm/dd/yyyy)").split("/")
# Open the weather data file to read
weatherData = open("../Lab 12/WeatherDataWindows.csv")

# Iterate through every line of the data file
for lines in weatherData:
    # Do not do anything with the header
    if row != 1:
        # Turns each row into a list of values
        rowList = lines.split(",")
        # Automatically assign the first high and low temperatures as the max and min
        if row == 2:
            maxTemp = int(rowList[1])
            minTmep = int(rowList[3])
        else:
            # If a temperature is higher than the max or lower than the min, then reassign the variables
            if int(rowList[1]) > maxTemp:
                maxTemp = int(rowList[1])
            elif int(rowList[3]) < minTemp:
                minTemp = int(rowList[3])
        # Store the precipitation column and total every value in it
        precipitation = rowList[-1]
        totalPrecip += float(precipitation)
        # Store the date for each row
        date = rowList[0].split("/")
        # If the row is for the date entered by the user, store the average dew point for that day
        if int(date[0]) == int(userDate[0]) and int(date[1]) == int(userDate[1]) and int(date[2]) == int(userDate[2]):
            storedAvgDepPoint = int(rowList[5])
        # Totals up the humidity highs for July
        if int(date[0]) == 7 and int(date[2]) == 2016:
            totalHumidityHigh += int(rowList[7])
        # Counts pressure low above 30
        if float(rowList[-2]) > 30:
            pressureAbove += 1
    # Increment the row variable
    row += 1

# Print the maximum and minimum temperatures
print("The highest recorded temperature over 3 years was", maxTemp, "degrees fahrenheit")
print("The lowest recorded temperature over 3 years was", minTemp, "degrees fahrenheit")

# Solve for average precipitation
avgPrecip = totalPrecip / (row - 1)
print("The average precipitation over 3 years was", avgPrecip, "in.")

print("The average dew point on", userDate[0], "/", userDate[1], "/", userDate[2], "was", storedAvgDepPoint,
      "degrees fahrenheit")

# Solve for average humidity high in July
avgHumidityHigh = totalHumidityHigh / 31
print("The average humidity high over 3 years in July 2016 was", avgHumidityHigh)

# Finds the percent of pressure lows above 30
percentPressure = pressureAbove / (row - 1) * 100
print("The percent of pressure lows above 30 over 3 years was", percentPressure, "%")

# Closes the file
weatherData.close()
