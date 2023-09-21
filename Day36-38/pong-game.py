from turtle import Turtle, Screen
from paddle import PaddleCreator
from ball import Ball
from scoreboard_pong import Scoreboard
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

#Crates a ball
ball = Ball()

#Creates scoreboard
scoreboard = Scoreboard()

#Paddle controls to move up and down
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

#Creates a loop that updates the screen
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect the collision with the walls past paddle
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(right_paddle) < 60 and ball.xcor() < 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
 
    #User Misses Ball with right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        

    #User Misses Ball with left paddle
    if ball.xcor() < -380:
        ball.reset_position() 
        scoreboard.r_point()
        scoreboard.update_scoreboard()


screen.exitonclick()