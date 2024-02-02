from tkinter import *
from tkinter import messagebox
import random

#Note: Command + / for = # block of code

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def make_password():
    #List of random letters, symbols, and numbers. 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #0-51
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] #0-8
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #0-9

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #Example of List Comprehension
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
   
    #Example of generating password with for loops
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    
    # for char in range(nr_symbols):
    #     password_list += (random.choice(symbols))

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    #Example 1 of password list
    # password = ""
    # for char in password_list:
    #     password += char

    #Example 2
    password = "".join(password_list)
    
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#When clicking the add button
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        #Standard Dialog - for a pop-up to check details of their inputs.
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok: 
            with open("Day47-password-manager/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

                #deleting from character 0 to the end of the entry, for new entries to be entered.
                website_input.delete(0, END)
                password_input.delete(0, END)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=50)

#Creates the canvas dimensions and adds the logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='Day47-password-manager/logo.png')
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