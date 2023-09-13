'''
Turtle Documentation:
https://docs.python.org/3/library/turtle.html

Trinket Turtle Colors:
https://trinket.io/docs/colors

Turtle Colors:
https://cs111.wellesley.edu/reference/colors

'''

from turtle import Turtle, Screen
from random import random

turtle = Turtle()

'''Makes the turtle shape'''
turtle.shape("turtle")

'''The turtle graphic will take this color'''
turtle.color("green")

'''The lines the turtle draws takes this color'''
turtle.pencolor("DarkOrchid")

'''Two ways to draw a square'''
# def square():
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)

for line in range(4):
    turtle.forward(100)
    turtle.left(90)


'''Spiral Spider Web with different colors.'''
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        turtle.color(c)
        turtle.forward(steps)
        turtle.right(30)


'''Star pattern'''
while True:
    turtle.forward(200)
    turtle.left(170)
    
      #Indicates if turtle is at home position
    if abs(turtle.pos()) < 1:
        break

'''Takes a random number of steps and angle'''
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    turtle.right(angle)
    turtle.forward(steps)


'''The undo() function'''
# for i in range(4):
#     turtle.fd(50); turtle.lt(80)

# for i in range(8):
#     turtle.undo()







#Needs to be on bottom
screen = Screen()
screen.exitonclick()
