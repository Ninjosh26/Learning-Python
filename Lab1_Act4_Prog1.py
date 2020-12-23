# Name: Josh Stafford
# Assignment: Lab 1b Activity 4 Program 1
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
from math import*

# (b) An interesting fact about myself
print("I have a cat, although I am allergic to them.")

# (c) Ohm's Law: Calculate the voltage across a conductor with resistance 20 ohms and a current of 5 A
print("The voltage is", 20*5, "V")

# (d) Kinetic Energy: Calculate the kinetic energy of an object with mass 100 kg and velocity 21 m/s
print("The kinetic energy is", 1/2*100*pow(21, 2), "J")

# (e) Reynolds Number(Re):  Calculate the Reynolds number for a fluid with velocity 100 m/s
# and kinematic viscosity 1.2 (m^2)/s, with characteristic linear dimension 2.5 m.
print("The Reynolds Number is", 100*2.5/1.2, "")

# (f) Arps equation: calculate the production of a well after 20 days, if it had an initial
# production rate of 100 barrels/day, an initial decline rate of 2 barrels/day, and a hyperbolic constant of 0.8.
print("The production of the well is", 100/(pow(1 + 0.8*2*20,1/0.8)), "barrels per day")

# (g) Mohr-Coulomb Failure Criterion: calculate the shear stress when a normal stress of 20 lbf/in^2 is applied
# to a material with cohesion 2 lbf/in^2 and angle of internal friction 35 degrees.
print("The shear stress is", 20*tan(radians(35)) + 2, "lbf/in^2")

