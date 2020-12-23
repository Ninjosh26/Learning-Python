# Name: Josh Stafford
# Assignment: Lab 12 Activity 2
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.
from turtle import *


def tallyMark():
    """ This function draws a single tally mark """
    pendown()
    forward(50)
    backward(50)
    penup()


def fiveTallyMark():
    """ This function draws a group of five tally marks """
    # Draws 5 tallies
    for i in range(4):
        tallyMark()
        left(90)
        forward(20)
        right(90)
    # Draws the diagonal
    forward(10)
    right(70)
    pendown()
    forward(100)
    penup()
    # Moves to next position to start drawing new tallies
    right(110)
    forward(44)
    right(90)
    forward(120)
    right(90)


def tallyMarkRow():
    """ This function draws a row of tallies, which contain 5 groups of 5 (or 25 tallies) """
    # Draws 5 groups of five
    for i in range(5):
        fiveTallyMark()
    # Moves to next row
    forward(70)
    right(90)
    forward(530)
    left(90)

# Sets the turtle to start in the top left
penup()
setx(-325)
sety(275)
right(90)
pendown()

# Asks the user to enter an amount of tallies they wish to draw
numTally = int(input("How many tallies would you like to draw?"))

# Draws until there are no more tallies to draw
while numTally > 0:
    # Tests if an entire row can be drawn
    if (numTally // 25) > 0:
        tallyMarkRow()
        numTally -= 25
    # Tests if a group of 5 can be drawn
    elif (numTally // 5) > 0:
        fiveTallyMark()
        numTally -= 5
    # Tests if single tallies can be drawn
    else:
        tallyMark()
        left(90)
        forward(20)
        right(90)
        numTally -= 1

# Keeps window open
input()
