# Name: Josh Stafford
# Assignment: Lab 1b Activity 4 Program 2
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
from math import *

# Function 1: f(x) = sin(x)/x
print("This shows the evaluation of sin(x)/x, evaluated close to x=0")
# guess
print("my guess is 1.0")
# calculated values
print(sin(1)/1)
print(sin(0.1)/0.1)
print(sin(0.01)/0.01)
print(sin(0.001)/0.001)
print(sin(0.0001)/0.0001)
print(sin(0.00001)/0.00001)
print(sin(0.000001)/0.000001)
print(sin(0.0000001)/0.0000001)
# space
print("")

# Function 2: 𝑔(𝑥) = (1―cos(𝑥))/𝑥^2
print("This shows the evaluation of (1―cos(𝑥))/𝑥^2, evaluated close to x=0")
# guess
print("my guess is 0.5")
# calculated values
print((1 - cos(1))/pow(1, 2))
print((1 - cos(0.1))/pow(0.1, 2))
print((1 - cos(0.01))/pow(0.01, 2))
print((1 - cos(0.001))/pow(0.001, 2))
print((1 - cos(0.0001))/pow(0.0001, 2))
print((1 - cos(0.00001))/pow(0.00001, 2))
print((1 - cos(0.000001))/pow(0.000001, 2))
print((1 - cos(0.0000001))/pow(0.0000001, 2))
# space
print("")

# Function 3: h(x) = (1+1/x)^x
print("This shows the evaluation of (1+1/x)^x, evaluated close to x=infinity")
# guess
print("my guess is e")
# calculated values
print(pow((1+1/1), 1))
print(pow((1+1/10), 10))
print(pow((1+1/100), 100))
print(pow((1+1/1000), 1000))
print(pow((1+1/10000), 10000))
print(pow((1+1/100000), 100000))
print(pow((1+1/1000000), 1000000))
print(pow((1+1/10000000), 10000000))


