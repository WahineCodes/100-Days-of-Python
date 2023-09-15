import colorgram 
import turtle as t
import random

'''Getting the rgb in a photo'''
# #How to call on an image in the same folder
# image = "100-Days-of-Python/Day31/image.jpg"

# # Extract colors from an image.
# rgb_colors = []
# colors = colorgram.extract(image, 30)


# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

'''
Requirements:
10 by 10 spots
20 in size - good
50 paces apart

'''
t.colormode(255)
t.speed("fastest")
t.penup()
t.setheading(225)
t.forward(400)
t.setheading(0)
t.hideturtle()

color_list = [(176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89), (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187), (131, 184, 161), (48, 187, 202), (172, 187, 222), (232, 173, 164), (154, 209, 219), (100, 51, 43), (34, 64, 115), (44, 80, 79), (215, 207, 37), (52, 58, 66)]

def random_color():
    random_number = random.randint(0, 25)
    r = int(color_list[random_number][0])
    g = int(color_list[random_number][1])
    b = int(color_list[random_number][2])
    the_color = (r, g, b)
    return the_color

t.penup()
t.goto(-300, -300)

def left_row():
    for i in range(1):
        t.penup()
        t.left(90)
        t.forward(70)
        t.left(90)
        t.forward(70)

def right_row():
    for i in range(1):
        t.penup()
        t.right(90)
        t.forward(70)
        t.right(90)
        t.forward(70)


def one_line():
    for i in range(10):
        t.dot(20, random_color())
        t.penup()
        t.forward(70)
        t.pendown()

for i in range(10):
    one_line()
    left_row()

    one_line()
    right_row()

    one_line()
    left_row()

    one_line()
    right_row()

    one_line()
    left_row()

    one_line()
    right_row()

    one_line()
    left_row()

    one_line()
    right_row()

    one_line()
    left_row()

    one_line()
    t.done()


 








screen = t.Screen()
screen.exitonclick()

