#Rosemary Davy
#February 25, 2021
#Problem 4: Write a Python function that takes a
#list of numbers and returns a new list with unique
#elements of the first list.Use list [1, 3, 3, 3, 6, 2, 3, 5].
#Use the appendfunction

def unique(y): #define how to determine if an item is unique
    y = []
    for i in list1:
        if i not in y:
            y.append(i)
    return y
 
list1 = [1, 3, 3, 3, 6, 2, 3, 5]

print("The unique values from the list are", unique(list1))
