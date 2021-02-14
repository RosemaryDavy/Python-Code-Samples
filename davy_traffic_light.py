#Rosemary Davy
#February 14, 2021
#This program draws a traffic light

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

alex.fillcolor("gray")

alex.begin_fill()               #draw the rectangle
for x in range(2):
    alex.forward(50)
    alex.right(90)
    alex.forward(200)
    alex.right(90)
alex.end_fill()

alex.penup ()                     #draw the circles
alex.forward(25)
alex.right(90)

lights = ("red" , "yellow" , "green")


for x in lights:
    alex.begin_fill()
    alex.forward(25)
    alex.right(90)
    alex.down()
    alex.circle(15)
    alex.fillcolor(x)
    alex.end_fill()
    alex.penup()
    alex.left(90)
    alex.forward(35)

    
    
