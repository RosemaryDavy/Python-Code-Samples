#Rosemary Davy
#February 25, 2021
#Problem 3: Write a Python function to
#multiply all the numbers in a list.
#Use list [5, 2, 7, -1].

def multiplyList(numbers): #define how to mulitply a list of numbers
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiplyList((5, 2, 7, -1)))
