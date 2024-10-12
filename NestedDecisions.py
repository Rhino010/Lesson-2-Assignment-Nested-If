# 1. Nested Decisions: The Adventure Game 🏰
# Objective: To practice the use of nested if statements.

# Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

# Original code
# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")

# Rectified code
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif place == "cave":
        print("You find a hidden treasure!")
    else:
        print("You found a boat!")


# Task 2: Setting the Scene

# Based on your corrected code from Task 1, 
# expand the game. If the user chooses "cave", 
# ask them if they want to "light a torch" or 
# "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? \n")

if place == "forest":
    action = input("climb a tree or cross a river?\n")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == 'cross a river':
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark?\n")
    if action == "proceed in the dark":
        print('You stub your toe. Should have a light bro.')
    elif action == "light a torch":
        print("You found treasure. Go enjoy yourself.")
    else:
        pass
else:
    pass
