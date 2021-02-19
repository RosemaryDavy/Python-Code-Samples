#Rosemary Davy
#February 19, 2021

import math
x = int(input("Enter your radian value: "))  #ask for user input in radians, make it an int, assign that value to x
y = (180 // (math.pi ** x))     #convert x to degrees
print(y) #print that value in degrees    
print(math.degrees(x)) #print the degrees value using the degrees function
