import tkinter

# Creating Window
window = tkinter.Tk()

# Change title
window.title("My First GUI Program")

# Change size
window.minsize(width=500, height=300)

# Create Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack() # Place and center it on the screen - defaults to side = "top"

# Keep window on Screen
window.mainloop()