# Name: Josh Stafford
# Assignment: Lab 10 Activity 3
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(18, 9))
# Establish point and array
v = [1, 0]
M = np.array([1.00583, -0.087156, 0.087156, 1.00583]).reshape(2, 2)
# Create lists for x and y values
xvalues = [1]
yvalues = [0]
# multiply the point and the matrix multiply times
for x in range(200):
    v = v @ M
    # Store the x and y values of each point
    xvalues.append(v[0])
    yvalues.append(v[1])
# Plot the points
plt.plot(xvalues, yvalues)
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle('Spiral')
plt.show()