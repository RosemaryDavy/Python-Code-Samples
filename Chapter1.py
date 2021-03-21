#Rosemary Davy

import time




def trainTalk():
    print("You: Hi, do you have any restaurant recommendations near Union Station?")
    time.sleep(2)
    print("Them: Yes, I recommend Native Foods. It's about a 10 minute walk from the station.")
    time.sleep(1)
    print("You: Wonderful, I'll check it out!")
    

def ch1choice():
    print("You have just sat down on a train to Chicago.")
    time.sleep(1)
    print("What would you like to do?")
    time.sleep(1)
    ch1choice = input("Press 1 to ask another passenger for restaurant recommendations or 2 to take a nap.")
    ch1choice == " "
    while ch1choice != "1" and ch1choice != "2":
        ch1choice = input("Press 1 to ask another passenger for restaurant recommendations or 2 to take a nap.")
    if ch1choice == "1":
        trainTalk()
    if ch1choice == "2":
        print("Okay. You will be there soon. Sleep well.")
        time.sleep(1)
    
        



#ch1choice()
