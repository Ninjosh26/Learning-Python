# Name: Josh Stafford
# Assignment: Lab 4 Activity 2b
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Asks user to input the amount of change
change = int(input("Enter the amount of change due in cents (1 to 499):"))
# Computes the coins to be dispensed
print("For $", float(change)/100, ", the coins to be dispensed are:", sep = "")
toonies = change//200
change -= toonies*200
loonies = change//100
change -= loonies*100
quarters = change//25
change -= quarters*25
dimes = change//10
change -= dimes*10
nickels = change//5
change -= nickels*5
pennies = change
# Prints the coins to be dispensed
print("toonies:", toonies)
print("loonies:", loonies)
print("quarters:", quarters)
print("dimes:", dimes)
print("nickels:", nickels)
print("pennies:", pennies)