from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clicked():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clicked():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    print(count)
    window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#The number countdown by
count_down(5)

#Timer Label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

#Tomato Image with countdown timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day46/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Start Button
start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_clicked)
start_button.grid(column=0,row=2)

#Reset Button
reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_clicked)
reset_button.grid(column=2, row=2)

#Check Mark
check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()