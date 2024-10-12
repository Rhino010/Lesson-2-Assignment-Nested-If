# 2. Quick Decisions: The Event Planner 🎉

# Task 1: Code Correction You are provided 
# with a Python script that is supposed to 
# help in event planning, but it has errors. 
# Identify and fix them.

# Original buddy code

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

# Rectified code
# attendees = int(input("Enter number of attendees: "))
# venue = print("large hall") if attendees > 100 else print("conference room")


# Task 2: Venue Selection

# Based on the corrected code from 
# Task 1, further enhance your code 
# to recommend additional things like 
# "audio system" or "projector" based 
# on the number of attendees.



attendees = int(input("Enter number of attendees: "))
venue = print("large hall") if attendees > 100 else print("conference room")
sound_system = print("You may want a full audio system in this large of a venue.") if attendees > 100 else print("The projector sound should be fine.")


# Task 3: Catering Choices

# Ask the user if they 
# want "vegetarian" food. Recommend 
# "Veggie Delight Caterers" if yes, 
# otherwise recommend "Gourmet Meals Caterers".

food = input("Would you like vegetarian food? Please type 'y' or 'n'\n")
caterer = print("You should use 'Veggie Delight Caterers") if food == 'y' else print("Gourmet Meals Caterers is a great choice.")
