from tkinter import *

def button_clicked():
    value = int(input.get())
    km = value * 1.609
    result_label.config(text=f"{km}")

window = Tk()
window.title("mi to km converter")
window.minsize(width=500, height=300)


# Label
equal_label = Label(text=f"is equal to", font=("Arial", 16, "bold"))
equal_label.grid(column=0, row=1)
km_label = Label(text="Km", font=("Arial", 16, "bold"))
km_label.grid(column=2, row=1)
result_label = Label(text="0", font=("Arial", 16, "bold"))
result_label.grid(column=1, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)
mi_label = Label(text="Miles", font=("Arial", 16, "bold"))
mi_label.grid(column=2, row=0)


window.mainloop()