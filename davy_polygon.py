#Rosemary Davy
#February 14, 2021
#This program asks the user for specs
#about a polygon
#and then draws the polygon
#the user designed

sides = int(input("How many sides do you want the polygon to be?"))
length = int(input("How long do you want the sides to be?"))
line_color = input("What color do you want the sides to be?")
fill = input("What color do you want the inside to be?")

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

alex.color(line_color)
alex.fillcolor(fill)

alex.begin_fill()
for x in range(sides):
    alex.forward(length)
    alex.right(360/sides)
alex.end_fill()



