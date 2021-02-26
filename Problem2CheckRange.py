#Rosemary Davy
#February 25, 2021
#Problem 2: Write a Python function to check whether a
#number is in a given range. Use range(1,10).
#Print whether the number is in or not in the range

import math

def checkRange(x): #define how to check if a number is in the range
    if num in range (1, 10):
        print("The number" , num , "is in the range (1,10).")
    else:
        print("The number" , num , "is outside the range (1,10).")

num = int(input("Please enter a number:"))
checkRange(num)


