'''
Title: Practice in Reeborgs World 
Description: Utilized the website https://reeborg.ca/index_en.html to practice and visualize how my code would execute. 
             Essentially your code needs to help Reeborg the robot reach the finish line, by completing different hurdles of varying levels.
             You can select the differnt hurdle levels on the tab bar above the animation.  
             Note that the code below pertain to the individual hurdle challenges can should be executed using the Reeborg's World platform to work.
             As a result, many of the functions below such as turn_left() or at_goal() are build-in functions in Reeborg's World. 
Practiced Using: def functions, for loop with range, while loops 
'''

#HURDLE 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    move()
    jump()

#HURDLE 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6

while number_of_hurdles > 0:
    if at_goal():
        done()
    
    else:
        move()
        jump()
        number_of_hurdles -= 1
        print(number_of_hurdles)


#HURDLE 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 20

while number_of_hurdles >0:
    if at_goal():
        done()
    elif wall_in_front():
        jump()
        number_of_hurdles -= 1
    elif front_is_clear():
        move()