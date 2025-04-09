from tkinter import *
from tkinter import messagebox
import random
import pyperclip
BACKGROUND = 'logo.png'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [
        random.choice(letters) for _ in range(random.randint(8, 10))
    ] + [
        random.choice(symbols) for _ in range(random.randint(2, 4))
    ] + [
        random.choice(numbers) for _ in range(random.randint(2, 4))
    ]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    if any(len(field) == 0 for field in [website, email, password]):
        messagebox.showerror(title='Oops!', message='Please fill in  all fields')
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                  f"\nPassword: {password}\nWould you like to save?")
    if is_ok:

        with open('data.txt', 'a') as file:
            file.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, END)
        email_user_entry.delete(0, END)
        email_user_entry.insert(0, "example@email.com")
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file=BACKGROUND)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username: ")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, 'example@email.com')

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)


#buttons
password_generation_button = Button(text='Generate Password', command=generate_password)
password_generation_button.grid(column=2, row=3)

add_button = Button(text='add', width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()