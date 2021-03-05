#Rosemary Davy
#March 4, 2021
#This function takes two inputs from a user
#and prints whether the sum is greater than 10,
#less than 10, or equal to 10.

def sum10():
    x = int(input("Please enter a whole number:"))
    y = int (input("Please enter another whole number:"))
    z = x + y

    if z > 10:
        print("The sum of the numbers you entered is greater than 10.")
    elif z < 10:
        print("The sum of the numbers you entered is less than 10.")
    else:
        print("The sum of the numbers you entered is equal to 10.")

sum10()
