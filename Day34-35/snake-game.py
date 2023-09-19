from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import random
import time

'''Setting up the screen'''
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

'''Calling the Classes'''
snake = Snake()
food = Food()
score = Score()

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

    #Detects when snake ate food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_to_score()
        
    #Detect the collision with the walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    #Detect the collision with the tail
        

    


screen.exitonclick()