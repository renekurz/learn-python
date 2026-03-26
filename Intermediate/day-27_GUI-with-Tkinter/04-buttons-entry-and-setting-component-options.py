from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="Type in a Name")

# Entry
input_field = Entry(width=10)
input_field.pack()

# Button
def button_clicked():
    name_label.config(text=f"Name: {input_field.get()}")

button = Button(text="Click me", command=button_clicked)
button.pack()

name_label = Label(text="", font=("Arial", 12, "normal"))
name_label.pack()

window.mainloop()