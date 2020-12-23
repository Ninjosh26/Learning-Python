# Name: Josh Stafford
# Assignment: Lab 6 Activity 2
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

scores = []
# Loop to collect score and player names until the list until user enters a negative number
while True:
    firstScore = int(input("Please the player's first round score, or enter a negative number to end the cycle:"))
    if firstScore < 0:
        break
    secondScore = int(input("Please the player's second round score:"))
    playerName = input("Please enter the player's name")
    # Adds values to scores list as a list containing the total score and player name
    scores.append([firstScore + secondScore, playerName])
print("")
# Sorts scores in ascending order
for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[i][0] > scores[j][0]:
            temp = scores[i]
            scores[i] = scores[j]
            scores[j] = temp
# Finds the median score
if len(scores) % 2 == 0:
    median = (scores[len(scores)//2][0] + scores[len(scores)//2 - 1][0]) / 2
else:
    median = scores[len(scores)//2][0]
# Prints the players that made the cut
print("The players that made the cut:")
for k in scores:
    if k[0] < median:
        print(k[1])
print("")
# Prints the players that did not make the cut
print("The players that did not make the cut:")
for k in scores:
    if k[0] >= median:
        print(k[1])