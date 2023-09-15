import colorgram 
import turtle as t
import random

'''
Requirements:
10 by 10 spots
20 in size - good
50 paces apart

'''
t.colormode(255)
color_list = [(176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89), (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187), (131, 184, 161), (48, 187, 202), (172, 187, 222), (232, 173, 164), (154, 209, 219), (100, 51, 43), (34, 64, 115), (44, 80, 79), (215, 207, 37), (52, 58, 66)]

t.speed("fastest")
t.penup()
t.setheading(225)
t.forward(400)
t.setheading(0)
number_of_dots = 100

t.hideturtle()

def random_color():
    random_number = random.randint(0, len(color_list)-1)
    r = int(color_list[random_number][0])
    g = int(color_list[random_number][1])
    b = int(color_list[random_number][2])
    the_color = (r, g, b)
    return the_color

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random_color())
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



screen = t.Screen()
screen.exitonclick()
