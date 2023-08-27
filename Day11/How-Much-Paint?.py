'''
Title: How Much Paint Do You Need?
Description: Finding out how much paint cans you need to cover a wall based on the users
             input of height and width. Note that one paint can, can cover 5 square meters. 
Practiced Using: def functions with more than one parameter and keyword arguments. 
'''
import math

def paint_calc(height, width, cover):
    number_of_cans = math.ceil((test_h * test_w)/cover)
    print(f"You'll need {number_of_cans} cans of paint.")

#The Parameters 
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

#Parameters with their arguments
paint_calc(height=test_h, width=test_w, cover=coverage)

