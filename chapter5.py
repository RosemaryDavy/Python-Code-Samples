#Rosemary Davy
import time
import chapter4

def ch5choice1():
    print("You are satisfied after a nice lunch. Now it’s time to explore Millennium Park.")
    time.sleep(2)
    print("There are musicians busking on the street corner.")
    time.sleep(1)
    ch5choice1 = input("Will you give them money? Press 1 for yes or 2 for no.")
    ch5choice1 == " "
    while ch5choice1 != "1" and ch5choice1 != "2":
        ch5choice1 = input("Will you give them money? Press 1 for yes or 2 for no.")
    if ch5choice1 == "1":
       print("That was nice of you! You received 2 extra hours of daylight.")
       time.sleep(1)
    if ch5choice1 == "2":
       print("Okay. Let's move on.")
       time.sleep(1)


def ch5choice2():
    print("Someone near you is getting robbed!")
    time.sleep(1)
    ch5choice2 = input("What will you do? Press 1 to help the victim or 2 to run away.")
    ch5choice2 == " "
    while ch5choice2 != "1" and ch5choice2 != "2":
        ch5choice2 = input("What will you do? Press 1 to help the vitim or 2 to run away.")
    if ch5choice2 == "1":
       print("You're a hero!")
       time.sleep(1)
       print("The victim is very appreciative and wants to take you to dinner as a thank you.")
    if ch5choice2 == "2":
       print("Run across the street to explore the park.")
  
#ch5choice1
#ch5choice2
    
