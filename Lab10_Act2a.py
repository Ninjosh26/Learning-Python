# Name: Josh Stafford
# Assignment: Lab 10 Activity 2a
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(18, 9))
# Bar Graph
plt.subplot(131)
plt.bar(['ducks', 'worms', 'fish', 'twigs'], [5.6, 2.1, 6.9, 3.3])
plt.ylabel('average per lake')
# Scatter Plot
plt.subplot(132)
plt.scatter([1, 2, 3, 4, 5, 6], [25, 62, 103, 91, 50, 10], c = '#ff7f0e')
plt.xlabel('students')
plt.ylabel('grades')
# Exponential graph
plt.subplot(133)
plt.plot([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 8, 16, 32, 64], c = '#2ca02c')
plt.xlabel('days')
plt.ylabel('test cases')

plt.show()