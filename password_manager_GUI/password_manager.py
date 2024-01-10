from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Creates the canvas dimensions and adds the logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='Day47/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

#Website input


#Email/Username input


#Password input


#Generate Password button


#Add button




#Must have this
window.mainloop()