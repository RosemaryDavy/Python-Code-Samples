#Rosemary Davy
#February 25, 2021
#draw 5 squares inside one another

import turtle

def drawSquare(t, sz): #definte how to draw 1 square
    """Get turtle t to draw a square of sz side"""
    for i in range (4):
        t.forward(sz)
        t.left(90)
    t.penup() #now make room to draw larger square
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()
        

wn = turtle.Screen() #set up alex

alex = turtle.Turtle()
alex.color("blue")

sz = 20
for i in range(5): #draw 5 squares, making them larger each time
    drawSquare(alex, sz + 20*i)

wn.exitonclick()
