from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        #Creates a 20 by 20 circle
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    #Ball goes off screen to the new coordinates
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font = ("Arial", 24, "normal"))


    
