#Rosemary Davy
#March 4, 2021
#This function takes a es a year as a parameter and 
#returns True if the year is a leap year, False if it is otherwise

year = int(input("Please enter a year:"))

def checkLeap(year):
    leap = False

    if year % 400 == 0 :
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap


print(checkLeap(year))

