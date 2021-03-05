#Rosemary Davy
#March 4, 2021
#This function takes two inputs
#from a user and prints whether they
#are equal or not

def equal():
    x = int(input("Please enter a whole number:"))
    y = int (input("Please enter another whole number:"))

    if x == y:
        print(x, "is equal to" , y, ".")
    else:
        print(x, "is not equal to" , y, ".")
equal()
