from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- X Button ------------------------------- #
def x_button():
    pass

# ---------------------------- Checkmark Button ------------------------------- #
def checkmark_button():
    pass

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)


#Creates the canvas
canvas = Canvas(height=526, width=800)
front_card = PhotoImage(file = "Day49-flash-card-app/card_front.png")

#Wrong
wrong_img = PhotoImage(file="Day49-flash-card-app/wrong.png")

wrong_button = Button(image=wrong_img, command=x_button)
wrong_button.grid(row=1, column=0)

#Right
right_img = PhotoImage(file="Day49-flash-card-app/right.png")

right_button = Button(image=right_img, command=checkmark_button)
right_button.grid(row=1, column=1)

window.mainloop()