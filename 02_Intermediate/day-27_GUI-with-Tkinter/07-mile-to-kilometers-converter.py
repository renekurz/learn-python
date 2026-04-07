from tkinter import *

FONT = ("Arial", 12, "normal")

def calculate():
    # name_label.config(text=f"Name: {input_field.get()}")
    miles = int(mile_input.get())
    km = miles * 1.60934
    output_label.config(text=int(km))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=125)

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to", font=FONT)
equal_to_label.grid(column=0, row=1)

output_label = Label(text="0", font=FONT)
output_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()