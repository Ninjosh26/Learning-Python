# Name: Josh Stafford
# Assignment: Lab 3 Activity 2
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Asks user to input words into the MadLib
years = input("Enter a number between 4 and 12:")
place = input("Enter a location:")
weeks = int(input("Enter a number:"))
# Converts weeks to days
days = weeks * 7
adjective = input("Enter an adjective:")
color = input("Enter a color:")
pluralNoun1 = input("Enter a plural noun:")
pluralNoun2 = input("Enter another plural noun:")
dayOfWeek = input("Enter a day of the week:")
# Prints the MadLib
print("When I was ", years, " years old, I loved to visit the ", place, ". About ", days, " days later, it had \n",
      "shut down, and I had to find a new favorite place. One day, I was walking through the city and I spotted a \n"
      , adjective, " ", color, " building.  It was so interesting, I had to go check it out! It was filled with\n",
      pluralNoun1, " and ", pluralNoun2, ". I could not believe my eyes. Now I go to visit there every ", dayOfWeek, "\n"
      "and it is my new favorite place.", sep="")
