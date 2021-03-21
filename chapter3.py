#Rosemary Davy
import time
import Chapter2

def ch3choice1():
    print("This is the most well-known building in Chicago. Dare to conquer you fear of heights.")
    time.sleep(1)
    print("What would you like to do?")
    time.sleep(1)
    ch3choice1 = input("Press 1 to go up to the sky deck or 2 to stay on the ground.")
    ch3choice1 == " "
    while ch3choice1 != "1" and ch3choice1 != "2":
        ch3choice1 = input("Press 1 to go up to the sky deck or 2 to stay on the ground.")
    if ch3choice1 == "1":
       print("Good for you for conquering your fear! You received a free Lyft credit to use whenever you like.")
    if ch3choice1 == "2":
        print("Okay. You can take photos of the building from down here.")
        time.sleep(1)

def ch3CircleBack():
    ch3choice1()
    print("Now what would you like to do?")
    time.sleep(1)
    ch3choice2 = input("Press 1 to walk to Native Foods or 2 to walk back to Union Station.")
    ch3choice2 == " "
    while ch3choice2 != "1" and ch3choice2 != "2":
        ch3choice2 = input("Press 1 to walk to Native Foods or 2 to walk back to Union Station.")
    if ch3choice2 == "1":
       print("Yum! Let's go!")
       time.sleep(1)
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
           time.sleep(1)
       if ch4choice1 == "2":
           print("You: Hi, how are you?")
           time.sleep(1)
           print("Them: I'm good. How are you?")
           time.sleep(1)
           print("You: I'm good. Do you want to come to Millenium Park with me? I've never been there.")
           time.sleep(1)
           print("Them: Sure, let's go!")
           time.sleep(1)
    if ch3choice2 == "2":
        print("Okay.")
        time.sleep(1)
        Chapter2.ch2choice1()
        Chapter2.ch2choice2()
    



def ch3choice2():
    print("Now what would you like to do?")
    time.sleep(1)
    ch3choice2 = input("Press 1 to walk to Native Foods or 2 to walk back to Union Station.")
    ch3choice2 == " "
    while ch3choice2 != "1" and ch3choice2 != "2":
        ch3choice2 = input("Press 1 to walk to Native Foods or 2 to walk back to Union Station.")
    if ch3choice2 == "1":
       print("Yum! Let's go!")
       time.sleep(1)
       
    if ch3choice2 == "2":
        print("Okay.")
        time.sleep(1)
        ch3CircleBack()

    
#ch3choice1()
#ch3choice2()

