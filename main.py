from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- SEARCH DATA ------------------------------- #


def search_data():
    website = web_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title=website, message="No Data File Found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {website} exist.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = web_entry.get()
    email_username = email_user_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email_username,
        "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels

web_label = Label(text='Website:')
web_label.grid(row=1, column=0)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

web_entry = Entry(width=20)
web_entry.grid(row=1, column=1)
web_entry.focus()
email_user_entry = Entry(width=45)
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_entry.insert(END, 'hellotwitter@gmail.com')
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

#  Buttons

generate_pass = Button(text="Generate Password", width=20, command=pass_generator)
generate_pass.grid(row=3, column=2, columnspan=1)

add = Button(text="Add", width=38, command=save_data)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=20, command=search_data)
search.grid(row=1, column=2)

window.mainloop()