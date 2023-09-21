from turtle import Turtle, Screen
from paddle import PaddleCreator
from ball import Ball
import time

#Setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Arcade Game")
screen.tracer(0)

#Creates two paddles
right_paddle = PaddleCreator((350, 0))
left_paddle = PaddleCreator((-350, 0))


#Paddle controls to move up and down
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


#Crates a ball
ball = Ball()


#Creates a loop that updates the screen
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    


screen.exitonclick()