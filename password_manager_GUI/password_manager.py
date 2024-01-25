from tkinter import *
from tkinter import messagebox

#Note: Command + / for = # block of code

# ---------------------------- Global Variables ------------------------------- #


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def make_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
#When clicking the add button
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    #Standard Dialog - for a pop-up to check details of their inputs
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    
    if is_ok: 
        with open("password_manager_GUI/data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            #deleting from 0 character to the end of the entry, so it can take the next entry.
            website_input.delete(0, END)
            password_input.delete(0, END)


        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=50)

#Creates the canvas dimensions and adds the logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='password_manager_GUI/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Website input 
website = Label(text="Website:")
website.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

#Email/Username input
email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "example@gmail.com")

#Password input
password = Label(text="Password:")
password.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

#Generate Password button
generator_button = Button(text="Generate Password", command=make_password)
generator_button.grid(row=3, column=2)

#Add button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)



#Must have this for the program to work
window.mainloop()