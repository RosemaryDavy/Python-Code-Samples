#Rosemary Davy
#March 4, 2021
#This function  checks whether a game character has
#picked up all the items needed to perform certain tasks and
#checks against any status debuffs

import random

items = ["pen", "paper", "idea", "rope", "groceries", "coat", "pan", "first aid kit"]
debuffs = ["slow", "small", "confusion"]


def mountain():
    print("MOUNTAIN:")
    y = random.sample(items, 3)
    x = random.choice(debuffs)
    print("Your supplies are:", y)
    print("Your debuff is:", x)
    mountainNeeds = ["rope", "coat", "first aid kit"]
    if mountainNeeds == y and x != "slow":
        print("You can climb the mountain.")
    elif mountainNeeds == y and x == "slow":
       print("You are too slow to climb the mountain.")
    else:
        print("You cannot climb the mountain.")
        
def meal():
    print("MEAL:")
    y = random.sample(items, 2)
    x = random.choice(debuffs)
    print("Your supplies are:", y)
    print("Your debuff is:", x)
    mealNeeds = ["pan", "groceries"]
    if mealNeeds == y and x != "small":
        print("You can cook a meal.")
    elif mealNeeds == y and x == "small":
        print("You cannot cook a meal.")
    else:
        print("You cannot cook a meal.")
 

def book():
    print("BOOK:")
    y = random.sample(items, 3)
    x = random.choice(debuffs)
    print("Your supplies are:", y)
    print("Your debuff is:", x)
    bookNeeds = ["pen", "paper", "idea"]
    if bookNeeds == y and x != "confusion":
        print("You can write a book.")
    elif bookNeeds == y and x == "confusion":
        print("You are too confused to write a book")
    else:
        print("You cannot write a book.")

mountain()
meal()
book()
    
