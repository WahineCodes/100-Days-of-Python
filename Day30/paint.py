import turtle as t
import random

turtle = t.Turtle()

turtle.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

'''Dashed line'''
# for i in range(20):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()
#     turtle.forward(10)

'''Drawing Shapes'''
# def shape(sides):
#     angle = 360/sides
#     for i in range(sides):
#         turtle.forward(100)
#         turtle.right(angle)
        

# for i in range(3, 11):
#     shape(i)

'''Random Angle and Steps'''
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     turtle.right(angle)
#     turtle.forward(steps)

'''Random Walk with color alternative'''
# directions = [0, 90, 180, 270]
# turtle.pensize(10)
# turtle.speed(10)

# for i in range(100):
#     for i in range(0, 4):
#         color = ["red", "pink", "purple", "green", "DeepSkyBlue"]
#         turtle.color(color[i])
#         turtle.forward(30)
#         turtle.setheading(random.choice(directions))


'''Random Walk alternative with tuple color'''
# directions = [0, 90, 180, 270]
# turtle.pensize(10)
# turtle.speed(10)

# for i in range(100):
#     turtle.color(random_color())
#     turtle.forward(30)
#     turtle.setheading(random.choice(directions))

'''Tuple - data type Ex. (1, 3, 8)'''
# my_tuple = (1, 3, 8)
# print(my_tuple[1])

'''Drawing a Spirograph Ex1'''
# turtle.speed("fastest")

# for i in range(2):
#     turtle.color(random_color())
#     turtle.circle(100)
#     turtle.right(5)

'''Drawing a Spirograph Ex2'''
turtle.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(5)



screen = t.Screen()
screen.exitonclick()
