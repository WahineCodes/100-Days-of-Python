from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")


#Converter Button
def converter_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609344
    km_result.config(text=f"{km}")

#Size of window
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

#Miles input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

#Miles Text
miles_text = Label(text="Miles", font=("Arial", 12, "bold"))
miles_text.grid(column=2, row=0)

#Is Equal to
is_equal_to = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to.grid(column=0, row=1)

#KM Result
km_result = Label(text="0", font=("Arial", 12, "bold"))
km_result.grid(column=1, row=1)

#KM text
km_text = Label(text="Km", font=("Arial", 12, "bold"))
km_text.grid(column=2, row=1)


#Button 
button = Button(text="Calculate", command=converter_clicked)
button.grid(column=1, row=2)


window.mainloop()


