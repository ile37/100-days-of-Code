from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#91C2AF"

def image_right():
    cards_data.drop(0, inplace=True)
    cards_data.reset_index(drop=True, inplace=True)
    save_progress()
    next_card()

def image_wrong():
    next_card()

def next_card():
    current_card_index = random.randint(0,len(cards_data)) - 1
    word_label.config(text=f"{cards_data['French'][current_card_index]}", bg="white", fg="black")
    language_label.config(text="French", bg="white", fg="black")
    canvas.create_image(400, 263, image=front_image)

    window.after(3000, turn_card, current_card_index)

def turn_card(index):
    canvas.create_image(400, 263, image=back_image)
    word_label.config(text=f"{cards_data['English'][index]}", bg=CARD_BACK_COLOR, fg="white")
    language_label.config(text="English", bg=CARD_BACK_COLOR, fg="white")

def save_progress():
    cards_data.to_csv("data/words_to learn.csv", index=False)
# ---------------------------- READ DATA ------------------------------- #
try:
    cards_data = pd.read_csv("data/french_words.csv")

except FileNotFoundError:
    print("File not found")

# ---------------------------- GUI ------------------------------- #

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=front_image)
canvas.grid(row=1, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=image_wrong)
wrong_button.grid(row=2, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=image_right)
right_button.grid(row=2, column=1)

# Labels
current_card_index = random.randint(0,len(cards_data)) - 1  
word_label = Label(text=f"{cards_data['French'][current_card_index]}", font=("Arial", 50, "italic"))
word_label.config(bg="white")
word_label.grid(row=1, column=0, columnspan=2)

language_label = Label(text="French", font=("Arial", 30, "italic"))
language_label.config(bg="white")
language_label.place(x=400, y=150, anchor="center")

window.after(3000, turn_card, current_card_index)

window.mainloop()
