from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.showturtle()
        

    #Controls Turtle to move up
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.forward(MOVE_DISTANCE)


    #Resets player to start after reaching the next level
    def reset_player(self):
        self.goto(STARTING_POSITION)