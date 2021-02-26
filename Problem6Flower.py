#Rosemary Davy
#February 25, 2021
#create flower

import turtle

def drawHexagon(t, sz): #define how to draw a hexagon
    """Get turtle t to draw a hexagon of sz side"""
    for i in range (6):
        t.forward(sz)
        t.left(60)

wn = turtle.Screen() #set up alex

alex = turtle.Turtle()
alex.color("pink")
alex.width(3)

sz = 45 #set size
for i in range(10): #create flower
    drawHexagon(alex, sz)
  
    alex.left(36)





wn.exitonclick()
