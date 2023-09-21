from turtle import Turtle, Screen

screen = Screen()

class PaddleCreator(Turtle):

    #Creates a paddle
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    #Paddle position
    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    #Paddle position
    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
