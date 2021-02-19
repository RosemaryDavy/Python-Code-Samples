#Rosemary Davy
#February 18, 2021

import math             #import math module
#Leibniz's formula for pi: x = 4 - (4/3) + (4/5) - (4/7) + (4/9)...

k = 1 #initialize denominator
s = 0 #initialize sum
for i in range(1000000):
    if i % 2 == 0: #even index elements are positive
        s += 4/k
    else:
        s -= 4/k #odd index elements are negative
    k += 2 #denominator increases by 2 each time
print(s) #print s
print(math.pi) #print the value of pi given by math module
