''''
Notes:
Headings = E = 0, N = 90, W = 180, S = 270

Documentation: https://docs.python.org/3/library/turtle.html#turtle.color
'''


from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

'''Creates six turtles'''
#Uses the index range to interact with the colors and y_position indices above
for turtle_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"{winning_color} turtle has won the race!")
            else:
                print(f"You've lost! The {winning_color} turtle has won the race!")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
