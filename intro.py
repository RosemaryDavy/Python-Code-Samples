#Rosemary Davy
import time
import sys
import Chapter1



def intro():
    player = input("Welcome! What is your name?")
    print("Hi," ,player, "!")
    time.sleep(1)
    print("You are about to explore Chicago for the first time!")
    time.sleep(1)
    print("You will visit famous tourist attractions and eat wonderful vegan food.")
    time.sleep(2)
    
def ready():
    ans = input("Are you ready to play? Press 1 for yes or 2 for no.")
    while ans != "1" and ans != "2":
        ans = input("Are you ready to play? Press 1 for yes or 2 for no.")
    if ans == "1":
       print("Great! Let's get started.")
    if ans == "2":
        print("Okay, bye.")
        sys.exit()


def ask_user():
    c = input("Would you like to continue playing? Press 1 for yes or 2 for no.")
    while c != "1" and c != "2":
        c = input("Are you ready to play? Press 1 for yes or 2 for no.")
    if c == "1":
       return
    if c == "2":
        print("Bye, thanks for playing.")
        sys.exit()








    



    
