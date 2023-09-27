import turtle
import pandas

#Screen Configurations
screen = turtle.Screen()
screen.title("U.S. States Game")

#Loads the turtle shape as an image, in this case the U.S.
image = "Day42/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Day42/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

game_on = True


while len(guessed_states) < 50:
    #Creates a pop-up window with question and input box
    answer_state = (screen.textinput(title = f"{len(guessed_states)}/50 State Correct", prompt = "What's another state's name?")).title()
    Font = ("Courier", 24, "normal")

    #Exit will break out of the loop and end the game
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day42/states_to_learn.csv")

        break

    #if statement that searches if the user_input matches any of the states in the dataframe
    if answer_state in all_states:
        guessed_states.append(answer_state)
        select_state = (data[data.state == str(answer_state)])
        
        #Get the x and y coordinate
        x_coor = int(select_state.x)
        y_coor = int(select_state.y)

        #Creates new writing turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coor, y_coor)
        t.write(answer_state)
    
    if len(guessed_states) == 50:
        t.goto(0, 0)
        t.write("Congradulations!", align = "center", font = Font)
        game_on = False





'''How to find the coordinates of each state'''
    # #Cordinates of each state based on x and y coordinates
    # def get_mouse_click_coor(x, y):
    #     print(x, y)

    # #litens to when the mouse clicks then passes over x, y click location
    # turtle.onscreenclick(get_mouse_click_coor)

    # #keeps the screen open so it doesnt exit
    # turtle.mainloop()

'''the item() function in pandas'''
    #item() grabs the first element
    # t.write(select_state.state.item())