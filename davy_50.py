#Rosemary Davy
#Februry 14, 2021
#Prints num 1-50
#if number is divisible by 3, it will say so
#if number is divisible by 5, it will say so
#if number is divisble by both, it will say so

num = list(range(1 , 51))

for x in num:
    if x % 3 == 0:
        print("Divisble by 3")
    elif x % 5 == 0:
        print("Divisble by 5")
    elif x % 3 == 0 and x % 5 == 0:
        print("Divisble by both")
    else:
        print(x)
