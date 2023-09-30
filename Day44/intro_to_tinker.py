import tkinter

#Creates a screen
window = tkinter.Tk()

window.title("My First GUI Program")

#Size of window
window.minsize(width=500, height=300)

#Adds text
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))

#Specify where the label will be on the screen
my_label.pack(side="left", expand = True)

#Keeps window on the screen like a loop. Needs to stay at end of the program
window.mainloop()