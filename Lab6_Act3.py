# Name: Josh Stafford
# Assignment: Lab 6 Activity 3
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Create the chess board
board = []
board.append(["R", "N", "B", "Q", "K", "B", "N", "R"])
board.append(["P", "P", "P", "P", "P", "P", "P", "P"])
board.append([".", ".", ".", ".", ".", ".", ".", "."])
board.append([".", ".", ".", ".", ".", ".", ".", "."])
board.append([".", ".", ".", ".", ".", ".", ".", "."])
board.append([".", ".", ".", ".", ".", ".", ".", "."])
board.append(["p", "p", "p", "p", "p", "p", "p", "p"])
board.append(["r", "n", "b", "q", "k", "b", "n", "r"])
while(True):
    # Print the chess board
    for i in board:
        for j in i:
            print(j, sep = "", end = "")
        print("")
    # Asks user which piece they would like to move
    print("Which piece would you like to move?")
    row = int(input("What row is it in (1-8)?"))
    column = int(input("What column is it in (1-8)?"))
    #Checks if there is a piece there
    if board[row - 1][column - 1] == ".":
        print("There are no pieces there")
        break
    # Asks user where they would like to move their piece
    print("Where would you like to move it?")
    row2 = int(input("What row would you like to move it to (1-8)?"))
    column2 = int(input("What column would you like to move it to (1-8)?"))
    # moves the piece to a new place
    board[row2 - 1][column2 - 1] = board[row - 1][column - 1]
    # Replaces the original spot with a empty spot
    board[row - 1][column - 1] = "."