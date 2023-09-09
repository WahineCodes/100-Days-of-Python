# import turtle

# '''taps into the turtle module and fetched the class Turtle
#    Note: classes are capital letter
   
#    Screen represents the screen object the turtle will show up in.

#    turtle documentation: https://docs.python.org/3/library/turtle.html
#    '''


# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")

# "changes turtle color"
# timmy.color("purple")

# '''Object Attributes'''
# my_screen = Screen()

# '''
# Example of syntax:
#  object   attribute
# my_screen.canvheight
# '''
# print(my_screen.canvheight)

# 'Bellow draws a triangle with timmy the turtle'
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)



# "Object Methods"
# my_screen.exitonclick()


'''Packages using pypi.org specifically prettytable:
How to intall: Go to terminal and type pip install prettytable

'''

from prettytable import PrettyTable

'''Creating an object called table'''
table = PrettyTable()

'''How to make columns
Columns: Pokemon Name and Type
'''

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

'''
print(table)

Creates:
+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+

'''


'''Object Attributes ~ table styles'''
'''Change it to left align, assigning the columns from "c" center to "l"'''
table.align = "l"
print(table)

