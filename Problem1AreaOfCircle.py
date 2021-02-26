#Rosemary Davy
#February 25, 2021
#Problem 1: Write a function areaOfCircle(r) which returns
#the area of a circle of radius r.
#Make sure you use the math module in your solution

import math

def areaCircle(x): #define how to calculate area of a circle using a radius
    a = 2 * math.pi * x
    return a
r = int(input("Please enter the radius of the circle:")) #ask user for radius
result = areaCircle(r)

print("The area of the cirle with a raidus of" , r , "is" , result , ".")
