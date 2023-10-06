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
#place() this is the top left corner, the y makes it go down
#positive x goes right
# Example: my_label.place(x=0, y=100)


'''alternative placement is using grid()'''
#____.grid(column=0, row=0) 
#Example, (column-0, row=1), (column=3, row=2)
#can think of it as a grid like chess squares
#Cant mix grid and pack in the same program
# column and row start at 0
my_label.grid(column=0, row=0)

'''Buttons, Entry, and Setting Component'''

#Two ways to change label name
my_label["text"] = "New Text"
my_label.config(text="New Text")


'''Button'''
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#Command is equivalent to turtle listen function
button = Button(text="Click Me", command=button_clicked)

#Pack allows it to be on the screen
#button.pack()
button.grid(column=1,row=1)


'''Entry Box'''
entry = Entry(width=30)

#Add some text to in the box to guide users entry
entry.insert(END, string="enter email please")
print(entry.get())
entry.grid(column=3, row=2)

#Baic entry box
input = Entry()

#place() puts the x and y value in a specific place
input.grid(column=3, row=3)


'''Text Box'''
text = Text(height=5, width=30)

#Puts cursor in textbox
text.focus()

#Adds some text to begin with
text.insert(END, "Example of multi-line entry box")

#Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(column=4, row=4)

'''Spinbox'''
def spinbox_used():
    #gets current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=0, row=2)


'''Scale'''
#Called with current scale value.
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=1, row=2)

'''Checkbutton'''
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


#variable to hold on to checked state, 0 is off, 1 is on.
#Need to use the IntVar()
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable = checked_state, command=checkbutton_used)
checked_state.get()
#checkbutton.pack()


'''Radiobutton'''
#Used to pick between two buttons

def radio_used():
    print(radio_state.get())

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
#radiobutton1.pack()
#radiobutton2.pack()


'''Listbox'''
def listbox_used(event):
    #Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

#Bind function used to call the def 
listbox.bind("<<ListboxSelect>>", listbox_used)
#listbox.pack(side="left")


'''pack()'''
#will always start from the first then pack them below each other, centered. 
#pack(side="left")

#Needs to stay at end of the program
#Keeps window on the screen like a loop. 
window.mainloop()
