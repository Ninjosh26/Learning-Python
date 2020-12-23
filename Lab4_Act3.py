# Name: Josh Stafford
# Assignment: Lab 4 Activity 3
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Part a
# Asks the user to enter a boolean value
booleana = input("input a boolean value (\"True\", \"T\", \'t\', \"False\", \"F\", \'f\'):")
# Converts input to boolean
if(booleana == "True" or booleana == "T" or booleana == 't'):
    booleanb = True
else:
    booleanb = False
# Checks if it works
if(booleanb):
    print("You entered True")
else:
    print("You entered False")

# Part b
# Asks the user to enter a boolean value for a
booleanInput = input("input a boolean value for a (\"True\", \"T\", \'t\', \"False\", \"F\", \'f\'):")
# Converts input to boolean
if(booleanInput == "True" or booleanInput == "T" or booleanInput == 't'):
    a = True
else:
    a = False
# Asks the user to enter a boolean value for b
booleanInput = input("input a boolean value for b (\"True\", \"T\", \'t\', \"False\", \"F\", \'f\'):")
# Converts input to boolean
if(booleanInput == "True" or booleanInput == "T" or booleanInput == 't'):
    b = True
else:
    b = False
# Asks the user to enter a boolean value for c
booleanInput = input("input a boolean value for c (\"True\", \"T\", \'t\', \"False\", \"F\", \'f\'):")
# Converts input to boolean
if(booleanInput == "True" or booleanInput == "T" or booleanInput == 't'):
    c = True
else:
    c = False
# Prints 1) a and b and c, 2) a or b or c
print("a and b and c is:", a and b and c)
print("a or b or c is:", a or b or c)

# Part c
# 1.
a = True
b = False
print((a or b) and not(a and b))
# 2.
a = False
b = False
c = True
first = a and b and c
second = (a and (not b) and (not c)) or (b and (not a) and (not c)) or (c and (not a) and (not b))
print(first or second)

# Part d
# Asks the user to enter a boolean value for a
booleanInput = input("input a boolean value for a (\"True\", \"T\", \'t\', \"False\", \"F\", \'f\'):")
# Converts input to boolean
if(booleanInput == "True" or booleanInput == "T" or booleanInput == 't'):
    a = True
else:
    a = False
# Asks the user to enter a boolean value for b
booleanInput = input("input a boolean value for b (\"True\", \"T\", \'t\', \"False\", \"F\", \'f\'):")
# Converts input to boolean
if(booleanInput == "True" or booleanInput == "T" or booleanInput == 't'):
    b = True
else:
    b = False
# Asks the user to enter a boolean value for c
booleanInput = input("input a boolean value for c (\"True\", \"T\", \'t\', \"False\", \"F\", \'f\'):")
# Converts input to boolean
if(booleanInput == "True" or booleanInput == "T" or booleanInput == 't'):
    c = True
else:
    c = False
# 1.
print((not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b))
# 2.
print((not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b
and c) or (a and ((b and not c) or (not b)))))
# Simplified
print((not b) or (not a and b and not c))
print(a or (not b and c))
