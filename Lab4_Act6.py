# Name: Josh Stafford
# Assignment: Lab 4 Activity 6
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Asks user to input a number of days
days = int(input("Please enter a number of days between 1 and 99:"))
# Establish starting widget value
widget = 0
# Check to see if user entered a valid number of days
if days > 0 and days < 100:
    # Calculate the amount of produced widgets and print them
    if days > 10:
        if days > 60:
            for x in range(days - 60):
                widget += (39 - x)
            widget += 2000
        else:
            widget = (days-10) * 40
        widget += 100
    else:
        widget = days * 10
    print("After", days, "days,", widget, "widgets are created")
else:
    print("You entered an invalid amount of days")