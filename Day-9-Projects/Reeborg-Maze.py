'''
Title: Practice in Reeborgs World 
Description: Utilized the website https://reeborg.ca/index_en.html to practice and visualize how my code would execute. 
             Essentially your code needs to help Reeborg the robot reach the finish line, by completing different hurdles of varying levels.
             You can select the differnt hurdle levels on the tab bar above the animation.  
             Note that the code below pertain to the individual hurdle challenges can should be executed using the Reeborg's World platform to work.
             As a result, many of the functions below such as turn_left() or at_goal() are build-in functions in Reeborg's World. 
Practiced Using: def functions, while loops 
'''

#HURDLE 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while True:
    if at_goal():
        done()
    elif right_is_clear() and wall_in_front():
        turn_right()
        move()
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        move()
    elif front_is_clear():
        move()
        if front_is_clear() and right_is_clear():
            turn_right()
            move()
    elif right_is_clear() and wall_in_front():
        turn_right()
        move()
