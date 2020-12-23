# Name: Josh Stafford
# Assignment: Lab 2b Program 1
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
from math import*

# (b) An interesting fact about myself
funFact = "I have a cat, although I am allergic to them."
print(funFact)

# (c) Ohm's Law: Calculate the voltage across a conductor with resistance 20 ohms and a current of 5 A
resistance = 20
current = 5
voltage = resistance * current
print("The voltage is", voltage, "V")

# (d) Kinetic Energy: Calculate the kinetic energy of an object with mass 100 kg and velocity 21 m/s
mass = 100
velocity = 21
kinetic = 1/2*mass*pow(velocity, 2)
print("The kinetic energy is", kinetic, "J")

# (e) Reynolds Number(Re):  Calculate the Reynolds number for a fluid with velocity 100 m/s
# and kinematic viscosity 1.2 (m^2)/s, with characteristic linear dimension 2.5 m.
velocity = 100
viscosity = 1.2
linearDimension = 2.5
reynolds = velocity * linearDimension / viscosity
print("The Reynolds Number is", reynolds, "")

# (f) Arps equation: calculate the production of a well after 20 days, if it had an initial
# production rate of 100 barrels/day, an initial decline rate of 2 barrels/day, and a hyperbolic constant of 0.8.
time = 20
productRate = 100
decRate = 2
hypbolicC = 0.8
arps = productRate/(pow(1 + hypbolicC*decRate*time, 1/hypbolicC))
print("The production of the well is", arps, "barrels per day")

# (g) Mohr-Coulomb Failure Criterion: calculate the shear stress when a normal stress of 20 lbf/in^2 is applied
# to a material with cohesion 2 lbf/in^2 and angle of internal friction 35 degrees.
nStress = 20
cohesion = 2
angle = 35
mohrCoulomb = nStress*tan(radians(angle)) + cohesion
print("The shear stress is", mohrCoulomb, "lbf/in^2")

