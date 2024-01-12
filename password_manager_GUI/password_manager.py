from tkinter import *

# ---------------------------- Global Variables ------------------------------- #


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def make_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Creates the canvas dimensions and adds the logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='password_manager_GUI/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Website input 
website = Label(text="Website:", font=("Arial", 12, "bold"))
website.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

#Email/Username input
email = Label(text="Email/Username:", font=("Arial", 12, "bold"))
email.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)

#Password input
password = Label(text="Password:", font=("Arial", 12, "bold"))
password.grid(row=3, column=0)

password_input = Entry(width=18)
password_input.grid(row=3, column=1)

#Generate Password button
generator_button = Button(text="Generate Password", command=make_password, width=15)
generator_button.grid(row=3, column=2)

#Add button
add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


#Must have this for the program to work
window.mainloop()