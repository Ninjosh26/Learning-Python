# Name: Josh Stafford
# Assignment: Lab 2 Activity 3
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
import math

# start distance in meters
distance1 = 50
# end distance in meters
distance2 = 615
# start time in seconds
time1 = 30
# end time in seconds
time2 = 45
slope = (distance2 - distance1) / (time2 - time1)
# input time
time = 37
# approximate value by linear interpolation
linearInterpolation = slope * (time - time1) + distance1
print("Distance from start at 37 seconds:", linearInterpolation)

print()
# Part 2
# start distance in meters
distance1 = 50
# end distance in meters
distance2 = 615
# start time in seconds
time1 = 30
# end time in seconds
time2 = 45
slope = (distance2 - distance1) / (time2 - time1)
# input time in seconds
time = 1200
# approximate value by linear interpolation
linearInterpolation = slope * (time - time1) + distance1
circumference = 1000 * math.pi
# print only the distance from the starting line
print("Distance from start at 20 minutes:", linearInterpolation % circumference)
