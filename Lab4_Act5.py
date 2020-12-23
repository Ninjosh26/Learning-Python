# Name: Josh Stafford
# Assignment: Lab 4 Activity 5
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Asks the user to input values for the Re equation
velocity = float(input("Please enter the characteristic velocity of the flow (m/s):"))
diameter = float(input("Please enter the pipe diameter (m):"))
viscosity = float(input("Please enter the fluid kinematic viscosity (m^2/s):"))
# Calculates the Re
reynolds = velocity * diameter / viscosity
# Prints the type of flow
if reynolds < 2300:
    print("The flow is laminar")
elif reynolds > 2900:
    print("The flow is turbulent")
else:
    print("The flow is in transition")