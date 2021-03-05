#Rosemary Davy
#March 4, 2021
#This function takes a list and prints if the value 5 is in that list.

def check5():
    x = input("Please enter a whole number:")
    y = input("Please enter another whole number:")
    z = input("Please enter another whole number:")
    num_list = list[x, y, z]
    print("The numbers you entered are:", num_list)
    num_list = str(num_list)
    if "5" in num_list :
       print("5 is in the list you created.")
    else:
       print("5 is not in the list you created.")
        



check5()


