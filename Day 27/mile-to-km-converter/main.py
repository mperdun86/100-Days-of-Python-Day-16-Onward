from tkinter import *

FONT = "Arial", 14, "normal"

def calc_mtk():
    miles = float(user_input.get())
    km = miles * 1.609
    kilometers.config(text=f"{km}")


window = Tk()
window.title('Mile to Kilometer Converter')
window.config(padx=20, pady=20)

user_input = Entry(width=7)
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text='is equal to', font=FONT)
is_equal_to_label.grid(column=0, row=1)

kilometers = Label(text='0', font=FONT)
kilometers.grid(column=1, row=1)

km_label= Label(text='Km', font=FONT)
km_label.grid(column=2, row=1)

calc_button = Button(text='Calculate', command=calc_mtk)
calc_button.grid(column=1, row=2)














window.mainloop()