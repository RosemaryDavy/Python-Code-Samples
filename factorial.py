#Rosemary Davy
#February 19, 2021

import math     #import math module
x = int(input("Please enter a value:"))     #ask user for inout value, make it an int, assign to x

z = 1
for i in range(1, x + 1): #for x number of times, multiply i by the previous product
    z = (z * i)
print("The factorial of ", x, " is ", z) #print statement
y = math.factorial(x) #calculate factorial of input with factorial function
print("The factorial of" , x, "is" , y) #print statement
