#Rosemary Davy
import time
import intro
import Chapter1


def ch2choice1():
    print("Your train has arrived at Union Station.")
    time.sleep(1)
    print("There are people asking for donations.")
    time.sleep(2)
    ch2choice1 = input("Will you give them money? Press 1 for yes or 2 for no.")
    ch2choice1 == " "
    while ch2choice1 != "1" and ch2choice1 != "2":
        ch2choice1 = input("Will you give them money? Press 1 for yes or 2 for no.")
    if ch2choice1 == "1":
       print("That was nice of you! You received 2 extra hours of daylight.")
       time.sleep(1)
    if ch2choice1 == "2":
        print("Okay. Let's move on.")
        time.sleep(1)
        
def ch2CircleBack():
    intro.intro()
    intro.ready()
    Chapter1.ch1choice()
    ch2choice1()
    print("Now what would you like to do?")
    time.sleep(1)
    print("You can take a train ride home or walk to the Sears Tower.")
    time.sleep(1)
    ch2choice2 = input("Press 1 to get on a train or 2 to go to the tower.")
    ch2choice2 == " "
    while ch2choice2 != "1" and ch2choice2 != "2":
        ch2choice2 = input("Press 1 to get on a train to go home or 2 to go to the tower.")
    if ch2choice2 == "1":
       print("Okay.")
       time.sleep(1)
       intro.ch2CircleBack()
    if ch2choice2 == "2":
        print("Okay. The Sears Tower is just down the street.")
        time.sleep(1)
      

def ch2choice2():
    print("Now what would you like to do?")
    time.sleep(1)
    print("You can take a train ride home or walk to the Sears Tower.")
    time.sleep(1)
    ch2choice2 = input("Press 1 to get on a train or 2 to go to the tower.")
    ch2choice2 == " "
    while ch2choice2 != "1" and ch2choice2 != "2":
        ch2choice2 = input("Press 1 to get on a train to go home or 2 to go to the tower.")
    if ch2choice2 == "1":
       print("Okay.")
       time.sleep(1)
       ch2CircleBack()
    if ch2choice2 == "2":
        print("Okay. The Sears Tower is just down the street.")
        time.sleep(1)







#ch2choice1()
#ch2choice2()

