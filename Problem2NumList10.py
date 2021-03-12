#Rosemary Davy
#March 11, 2021
#Problem 2: Using a while loop, create a list called L that contains the numbers 0 to 10.
#On each iteration, the loop should append the current value of a counter
#variable to the list and then increase the counter by 1.
#The while loop should stop once the counter variable is greater than 10.

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 0
while c <= 10:
    L.append(c)
    c = c + 1
    
print(L) #to check if the loop worked
    
