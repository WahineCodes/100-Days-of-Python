from tkinter import *

'''Since we imported all we don't have to add tkinter like below'''
# window = tkinter.Tk()
# window.title("My First GUI Program")

#Creates a screen
window = Tk()
window.title("My First GUI Program")

#Size of window
window.minsize(width=500, height=300)

#Adds text
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))

#Specify where the label will be on the screen
# my_label.pack(side="left", expand = True)
my_label.pack()


'''Buttons, Entry, and Setting Component'''

#Two ways to change label name
my_label["text"] = "New Text"
my_label.config(text="New Text")


'''Button'''
def button_clicked():
    print("I got clicked")
    my_label["text"] = "Button Got Clicked"

#Command is equivalent to turtle listen function
button = Button(text="Click Me", command=button_clicked)

#Pack allows it to be on the screen
button.pack()


'''Entry Box'''
input = Entry()
input.pack()



#Needs to stay at end of the program
#Keeps window on the screen like a loop. 
window.mainloop()
