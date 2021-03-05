from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # `


def button_start_clicked():
    print("x")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def button_start_clicked():
    start_timer();


count = 5
def start_timer():
    count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_second = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
my_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
my_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))


button_start = Button(text="start", highlightthickness=0, command=button_start_clicked)
button_start.grid(column=0, row=3)

button_reset = Button(text="reset", highlightthickness=0, command=button_start_clicked)
button_reset.grid(column=3, row=3)


check_label = Label(text="✔", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=4)

window.mainloop()