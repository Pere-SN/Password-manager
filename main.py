from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered:\nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data_cc.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=30)
window.minsize(width=400, height=380)

# Canvas
canvas = Canvas(width=200, height=200)
pomodoro_img = PhotoImage(file="logo.png")
canvas.create_image(70, 100, image=pomodoro_img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:", font=("Helvetica", 10, "bold"))
website_label.grid(row=1, column=0, sticky="e")

email_label = Label(text="Email/Username:", font=("Helvetica", 10, "bold"))
email_label.grid(row=2, column=0, sticky="e")

password_label = Label(text="Password:", font=("Helvetica", 10, "bold"))
password_label.grid(row=3, column=0, sticky="e")

# Entry
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=17)
password_entry.grid(row=3, column=1, sticky="w")

# Button
generate_button = Button(text="Generate Password", command=pass_generator)
generate_button.grid(row=3, column=1, columnspan=2, sticky="e")

add_button = Button(text="Add", width=30, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()
