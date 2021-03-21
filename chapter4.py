#Rosemary Davy
import time
import Chapter2
import chapter3


def befriend():
     print("You: Hi, how are you?")
     time.sleep(1)
     print("Them: I'm good. How are you?")
     time.sleep(1)
     print("You: I'm good. Do you want to come to Millenium Park with me? I've never been there.")
     time.sleep(1)
     print("Them: Sure, let's go!")
     time.sleep(1)

def ch4choice1():
    print("You are very hungry now, but can’t stay long because there are other places to see.")
    time.sleep(2)
    print("The Watermelon Fresca will be refreshing!")
    time.sleep(1)
    print("What would you like to do?")
    time.sleep(1)
    ch4choice1 = input("Press 1 to eat lunch or 2 to befriend people in the cafe.")
    ch4choice1 == " "
    while ch4choice1 != "1" and ch4choice1 != "2":
        ch4choice1 = input("Press 1 to eat lunch or 2 to befriend people in the cafe.")
    if ch4choice1 == "1":
       print("Yum. Enjoy your lunch!.")
       time.sleep(2)
    if ch4choice1 == "2":
       befriend()


def ch4CircleBack():
     ch4choice1()
     print("Lunchtime is over.")
     time.sleep(1)
     print("Now you can go to Millenium Park or go back to Union Station.")
     time.sleep(1)
     print("What would you like to do?")
     time.sleep(1)
     ch4choice2 = input("Press 1 to walk to the park or 2 to go back to Union Station.")
     ch4choice2 == " "
     while ch4choice2 != "1" and ch4choice2 != "2":
          ch4choice2 = input("Press 1 to walk to the park or 2 to go back to Union Station.")
     if ch4choice2 == "1":
          print("The park will be fun!")
          time.sleep(1)
     if ch4choice2 == "2":
          Chapter2.ch2choice1()
          Chapter2.ch2choice2()
          chapter3.ch3choice1()
          chapter3.ch3choice2()

       
def ch4choice2():
    print("Lunchtime is over.")
    time.sleep(1)
    print("Now you can go to Millenium Park or go back to Union Station.")
    time.sleep(1)
    print("What would you like to do?")
    time.sleep(1)
    ch4choice2 = input("Press 1 to walk to the park or 2 to go back to Union Station.")
    ch4choice2 == " "
    while ch4choice2 != "1" and ch4choice2 != "2":
        ch4choice2 = input("Press 1 to walk to the park or 2 to go back to Union Station.")
    if ch4choice2 == "1":
       print("The park will be fun!")
       time.sleep(1)
    if ch4choice2 == "2":
       Chapter2.ch2choice1()
       Chapter2.ch2choice2()
       chapter3.ch3choice1()
       chapter3.ch3choice2()
       ch4CircleBack()
       


#ch4choice1
#ch4choice2


    
