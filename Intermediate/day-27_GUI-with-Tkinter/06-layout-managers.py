from tkinter import *

def button_clicked():
    name_label.config(text=f"Name: {input_field.get()}")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.place(x=0, y=0) # top left corner
my_label.grid(column=0, row=0) # top left corner

my_label["text"] = "New text"
my_label.config(text="Type in a Name")

input_field = Entry(width=10)
input_field.grid(column=0, row=1)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

name_label = Label(text="", font=("Arial", 12, "normal"))
name_label.grid(column=0, row=2)

# my_label.pack()
# input_field.pack()
# button.pack()
# name_label.pack()

window.mainloop()