from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    error_string = ""
    if website == "":
        error_string += "website / "
    if email == "":
        error_string += "email / "
    if password == "":
        error_string += "password"
    if error_string != "":
        messagebox.showerror(title="ERROR", message=f"You forgot to enter {error_string}")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
    
    if is_ok:
        with open("data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)

        messagebox.showinfo(title="Saved Successful", message=f"Password for {website} saved!")

            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_input = Entry(width=35)
website_label.grid(column=0, row=1)
website_input.grid(column=1, row=1, columnspan=2)

# Email/Username
email_label = Label(text="Email/Username:")
email_input = Entry(width=35)
email_input.insert(0, "jon@doe.com")
email_label.grid(column=0, row=2)
email_input.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password:")
password_input = Entry(width=21)
generate_password_button = Button(text="Generate Password", command=generate_password, width=11)
password_label.grid(column=0, row=3)
password_input.grid(column=1, row=3)
generate_password_button.grid(column=2, row=3)

# Add
add_password_button = Button(text="Add", command=save_password, width=36)
add_password_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
