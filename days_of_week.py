print("Suppose each day of the week is assigned a number 0-6, where Sunday is 0, Monday is 1, etc, all the way to Saturday being 6.")
string_leave = input("What day are you leaving? Answer with a digit 0-6: ")
int_leave = int(string_leave)
string_length = input("How many days is your trip?: ")
int_length = int(string_length)

day_return = (int_leave + int_length) % 7

print("You will come back on day: ", day_return)


#Rosemary Davy
#January 28, 2021
#This program asks the user for the day they are leaving and the number of days they will be gone.
#It then tells the on what day they will return.
