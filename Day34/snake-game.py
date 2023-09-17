from turtle import Turtle, Screen
from snake import Snake
import random
import time

'''Setting up the screen'''
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

'''Calling the Snake class'''
snake = Snake()

'''Controlling the snake's direction'''
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


'''Make all Snake parts forward'''
game_is_on = True
while game_is_on:
    #Updates the screen only when below goes through
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()