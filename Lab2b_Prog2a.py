# Name: Josh Stafford
# Assignment: Lab 2b Program 2a
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# time start
time1 = 13
# time finish
time2 = 84
# first coordinate
x1 = 1
y1 = 3
z1 = 7
# second coordinate
x2 = 23
y2 = -5
z2 = 10
timeOfInterest = 50
# calculating position at time of interest
x = (x2 - x1) / (time2 - time1) * (timeOfInterest - time1) + x1
y = (y2 - y1) / (time2 - time1) * (timeOfInterest - time1) + y1
z = (z2 - z1) / (time2 - time1) * (timeOfInterest - time1) + z1
# print values
print("time of interest =", timeOfInterest, "seconds")
print("x0 =", x, "m")
print("y0 =", y, "m")
print("z0 =", z, "m")
