#Rosemary Davy
#March 11, 2021
#Problem 3: Using a while loop, ask the user to enter a number.
#Append each entered number to a list and add them together.
#Continue asking for a number until the sum of the list of numbers is greater than 100

L = []

while sum(L) <= 100:
   num =  int(input("Please enter a number:"))
   L.append(num)

print(L)
