# Name: Josh Stafford
# Assignment: Lab 10 Activity 2b
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

plt.figure(figsize=(18, 9))
# Histogram
plt.subplot(131)
x = [np.random.randn(7000), np.random.randn(3000)]
plt.hist(x, 200, facecolor='r', alpha=1)
plt.xlabel('Entropy')
plt.ylabel('Temperature')
# Graph with multiple data sets
plt.subplot(132)
plt.plot([1, 2, 3, 4], [3, 4, 9, 12], 'y^', [1, 2, 3, 4], [2, 4, 6, 8], 'bo', [1, 2, 3, 4], [8, 6, 4, 2], 'rp-')
yellow_patch = mpatches.Patch(color='yellow', label='group1')
blue_patch = mpatches.Patch(color='blue', label='group2')
red_patch = mpatches.Patch(color='red', label='group3')
plt.legend(handles=[yellow_patch, blue_patch, red_patch], loc='upper left')
plt.xlabel('people')
plt.ylabel('sandwiches')
# Cosine wave
plt.subplot(133)
theta = np.arange(0.0, 20.0, 0.08)
plt.plot(theta, np.cos(theta)*0.5, 'g-')
plt.xlabel('time')
plt.ylabel('position')

plt.show()