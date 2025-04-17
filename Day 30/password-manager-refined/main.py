from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if any(len(field) == 0 for field in [website, email, password]):
        messagebox.showerror(title='Oops!', message='Please fill in  all fields')
        return
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH FUNCTIONALITY ------------------------------- #
def find_password():
    search_term = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found.')
    else:
        if search_term in data:
            messagebox.showinfo(title=search_term, message=f'Email/Login: {data[search_term]["email"]}\nPassword: {data[search_term]["password"]}')
        else:
            messagebox.showerror(title='Error', message=f'No details for "{search_term}" exists')



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
website_entry = Entry(width=26)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_user_entry = Entry(width=44)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, 'example@email.com')

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

# Buttons
password_generation_button = Button(text='Generate Password', command=generate_password)
password_generation_button.grid(column=2, row=3)

add_button = Button(text='add', width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(column=2, row= 1)

window.mainloop()