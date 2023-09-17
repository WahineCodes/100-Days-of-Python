from turtle import Turtle

#Constances makes it easier to modify in the future
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]
    

    #Creates three snakes with unique positions
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.all_snakes.append(new_snake)

    def move(self):
        #Logic: have each snake take the place of the previous one.
        #step, stop, start based on the starting_position visualize: range(start=2, stop=0, step=1)
        for snake_number in range(len(self.all_snakes)-1, 0, -1):
            new_x = self.all_snakes[snake_number - 1].xcor()
            new_y = self.all_snakes[snake_number - 1].ycor()
            self.all_snakes[snake_number].goto(new_x, new_y)
            
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        #heading refers to the self.all_snake[0] or the first snake
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
