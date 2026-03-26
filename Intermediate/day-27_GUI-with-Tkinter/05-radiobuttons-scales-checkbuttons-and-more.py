from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))

my_label["text"] = "New text"
my_label.config(text="Type in a Name")

input_field = Entry(width=10)

def button_clicked():
    name_label.config(text=f"Name: {input_field.get()}")

button = Button(text="Click me", command=button_clicked)

name_label = Label(text="", font=("Arial", 12, "normal"))

# Textbox
text_box = Text(height=5, width=30)

# Puts cursor in textbox
text_box.focus()

# Adds some text to begin with
text_box.insert(END, "Example of multi-line text entry")

# Get's current value in textbox at line 1, character 0
print(text_box.get("1.0", END))

# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)

# Scale
# Called with current scale value
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)

# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

# variable to hold on to checked state, 0 is off, 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()

# Radiobutton
def radio_used():
    print(radio_state.get())

# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton_1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton_2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)

# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)

my_label.pack()
input_field.pack()
button.pack()
name_label.pack()
text_box.pack()
spinbox.pack()
scale.pack()
checkbutton.pack()
radiobutton_1.pack()
radiobutton_2.pack()
listbox.pack()

window.mainloop()
