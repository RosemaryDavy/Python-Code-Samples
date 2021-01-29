string_miles = input("How many miles did you travel?")
float_miles = float(string_miles)
string_gallons = input("How many gallons of gas did you use?")
float_gallons = float(string_gallons)
mpg = float_miles // float_gallons
print("Your car can travel approximately" , mpg , "miles per gallon of gasoline.")

#Rosemary Davy
#January 28, 2021
#This program asks the user for the number of miles they drove and the number of gallons of gasoline used.
#It then converts that into miles per gallon and tells the user the result.
