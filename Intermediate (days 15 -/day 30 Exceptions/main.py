from tkinter import *
from tkinter import messagebox
import password_gen
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = password_gen.password_generator()
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_site = web_site_entry.get()
    password = password_entry.get()
    username = username_entry.get()

    if len(web_site) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oopsy", message="Please don't leave any fields empty!")
        return
    
    new_entry = {
            web_site: {
                "email": username,
                "password": password
            }
        }

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        with open("data.json", mode="w") as file:
            json.dump(new_entry, file, indent=4)

    # File exists but is empty
    except json.decoder.JSONDecodeError:
        with open("data.json", mode="w") as file:
            json.dump(new_entry, file, indent=4)

    else:        
        data.update(new_entry)
        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)

    finally:
        clear()

def clear():
    web_site_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- Search ------------------------------- #
def search():
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oopsy", message="No Data File Found.")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Oopsy", message="Data file is empty.")
    else:
        web_site = web_site_entry.get()
        if web_site in data:
            messagebox.showinfo(title=web_site, message=f"Email: {data[web_site]['email']}\nPassword: {data[web_site]['password']}")
        else:
            messagebox.showinfo(title="Oopsy", message=f"No details for {web_site} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

web_site_label = Label(text="Website:")
web_site_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

web_site_entry = Entry(width=21)
web_site_entry.focus()
web_site_entry.grid(column=1, row=1)

username_entry = Entry(width=40)
username_entry.insert(0, "your.email@test.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate password", command=generate_password)
generate_password_button.config(width=15, height=1)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)


window.mainloop()