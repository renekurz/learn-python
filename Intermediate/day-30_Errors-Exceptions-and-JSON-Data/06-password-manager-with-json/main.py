from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json     #TODO: import json

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
    
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    #! Uncomment if you want to write
    # with open("data.json", mode="w") as file: # TODO-1: edit to write in a json file
    #     json.dump(new_data, file, indent=4)

    #     website_input.delete(0, END)
    #     password_input.delete(0, END)

    #! Uncomment if you want to read
    # with open("data.json", mode="r") as file: # TODO-2: edit to read from a json file
    #     data = json.load(file)
    #     print(data)

    #     website_input.delete(0, END)
    #     password_input.delete(0, END)

    #TODO-3: This will create and update the data.json, so you don't need the create function
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)

        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)

    messagebox.showinfo(title="Saved Successful", message=f"Password for {website} saved!")

# ------------------------- SEARCH WEBSITE ---------------------------- #
def search_website():
    website = website_input.get()

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            searched_data = data[website]
    except FileNotFoundError as file_not_found_error:
        messagebox.showerror(title=file_not_found_error, message="Please create a password! There are no safed passwords.")
    except KeyError as key_error:
        messagebox.showerror(title=key_error, message="Please enter a login for this Website! There is no login for this Website yet.")
    else:
        email_input.delete(0, END)
        password_input.delete(0, END)

        email_input.insert(0, searched_data["email"])
        password_input.insert(0, searched_data["password"])

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
website_input = Entry(width=21)
website_search_button = Button(text="Search", command=search_website, width=11)
website_label.grid(column=0, row=1)
website_search_button.grid(column=2, row=1)
website_input.grid(column=1, row=1)

# Email/Username
email_label = Label(text="Email/Username:")
email_input = Entry(width=37)
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
