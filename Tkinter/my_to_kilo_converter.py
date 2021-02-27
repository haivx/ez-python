from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)


def convert():
    miles = miles_input.get()
    result = float(miles) * 1.6
    result_label.config(text=result)


my_label = Label(text='Miles')
my_label.grid(column=2, row=0)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)


km_label = Label(text="km")
km_label.grid(column=2, row=1)


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()