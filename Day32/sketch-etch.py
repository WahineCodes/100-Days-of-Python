from turtle import Turtle, Screen

t = Turtle()
screen = Screen()



def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def clear_drawing():
    screen.clearscreen()
    t.penup()
    t.home()
    t.pendown()

screen.listen()

'''Example of using a function in a function'''
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()
