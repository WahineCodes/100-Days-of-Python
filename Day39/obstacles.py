from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

RANDOM_INTEGER = random.randint(1, 25)

class Obstacles():
    
    def __init__(self):
        self.all_obstacles = []
        self.car_speed = STARTING_MOVE_DISTANCE

    
    def create_obstacle(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_block = Turtle("square")
            new_block.shapesize(stretch_wid = 1, stretch_len=2)
            new_block.penup()
            new_block.color(random.choice(COLORS))

            new_y = random.randint(-250, 250)
            new_block.goto(300, new_y)
    
            self.all_obstacles.append(new_block)

    def move_obstacle(self):
        for obstacle in self.all_obstacles:
            obstacle.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
    