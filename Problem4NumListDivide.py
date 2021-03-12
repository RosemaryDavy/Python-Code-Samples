#Rosemary Davy
#March 11, 2021
#Problem 4: Create a while loop that initializes a counter at 0 and will run until the counter reaches 50.
#If the value of the counter is divisible by 10, append the value to the list called tens.
#Confirm the list results using a print statement

tens = []
c = 0
while c < 50:
    c = c + 1
    if c % 10 == 0:
        tens.append(c)
print(tens)
        
