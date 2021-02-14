#Rosemary Davy
#February 13, 2021
#This program prints each number in list
#on its own line

num = [12, 10 , 32 , 3 , 66 , 17 , 42 , 99 , 20]
for x in num:
    print(x)
    
#and also prints the given numbers along with their square
#on a new line

squared = [ ]

for x in num:
    sqr = x * x
    squared.append(sqr)
    print("The square of {} is {}".format(x, sqr))
