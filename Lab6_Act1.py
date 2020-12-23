# Name: Josh Stafford
# Assignment: Lab 6 Activity 1
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Starting values
production = []
# Loop to collect values until the list until user enters a negative number
while True:
    data = int(input("Please enter the production level for the day, or enter a negative number to end the cycle:"))
    if data < 0:
        break
    production.append(data)
# Counting variables
count = 0
increasing = 0
decreasing = 0
# Loop through all intervals and determine if they are increasing or decreasing
for i in range(1, len(production)):
    for j in range(0, len(production) - i):
        interval = production[j + i] - production[j]
        if interval > 0:
            increasing += 1
        elif interval < 0:
            decreasing += 1
        count += 1
    # Calculate the percent of increasing and decreasing intervals
    increasePerc = increasing / count * 100
    decreasePerc = decreasing / count * 100
    # Print the intervals and the percentage of increasing and decreasing
    print("For ", i, "-day intervals ", round(increasePerc, 1), "% were increasing and "
          , round(decreasePerc, 1), "% were decreasing", sep = "")
    # Reset the counting variables
    count = 0
    increasing = 0
    decreasing = 0
