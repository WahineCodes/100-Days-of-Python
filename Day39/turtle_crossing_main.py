from turtle import Turtle, Screen
from turtle_figure import Player
from scoreboard import Scoreboard
from obstacles import Obstacles
import random
import time

player = Player()
scoreboard = Scoreboard()
obstacles = Obstacles()

#Screen Dimensions
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.update()

screen.listen()
screen.onkey(player.go_up, "Up")

#Game loop
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    obstacles.create_obstacle()
    obstacles.move_obstacle()

    #Turtle collision with a obstacle
    for obstacle in obstacles.all_obstacles:
        if obstacle.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Turtle reaches the finish line
    if player.ycor() > 280:
        scoreboard.level_up()
        obstacles.increase_speed()
        player.reset_player()
        scoreboard.update_scoreboard()

    

    

screen.exitonclick()