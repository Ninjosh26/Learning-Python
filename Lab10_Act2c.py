# Name: Josh Stafford
# Assignment: Lab 10 Activity 2c
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9, 9))
# 2 Quadratic functions
plt.subplot(121)
x = np.arange(-10, 10, 0.1)
plt.plot(x, x**2, 'b--', x, -x**2, 'o-')
plt.xlabel('x')
plt.ylabel('y')
# Random scatter plot
plt.subplot(122)
x = np.arange(0, 1000, 2)
plt.plot(x, np.random.rand(500), 'b^')
plt.xlabel('readings')
plt.ylabel('precipitation')
plt.show()