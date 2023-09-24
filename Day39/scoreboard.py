from turtle import Turtle, Screen
from obstacles import Obstacles

obstacles = Obstacles()

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level {self.level}", align = "left", font = FONT)


    #When the level goes up the move_increment of the blocks will increase as well
    def level_up(self):
        self.level += 1


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font = ("Courier", 24, "normal"))

