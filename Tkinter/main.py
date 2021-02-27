from tkinter import *

window = Tk()
window.title("My first program")
window.minsize(width=500, height=300)

my_label = Label(text='I am a label')
my_label.config(text='new text')
my_label.grid(column=0, row=1)


def button_clicked():
    print(button.get())


button = Button(text="click me", command=button_clicked)
button.grid(column=3, row=1)

button = Button(text="new me", command=button_clicked)
button.grid(column=2, row=2)

input = Entry(width=10)
input.grid(column=4, row=3)


window.mainloop()
