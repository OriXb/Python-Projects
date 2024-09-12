from tkinter import *
import pandas
import random
import os

# Const & Vars

BACKGROUND_COLOR = "#B1DDC6"
WORD_FONT = ("Ariel", 60, "bold")
LANG_FONT = ("Ariel", 40, "bold")


# Database import

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    os.remove("data/words_to_learn.csv")
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")

choosen_card = {}


# Game Code

def new_card():
    try:
        global choosen_card
        global flip_timer
        window.after_cancel(flip_timer)
        choosen_card = random.choice(data_dict)
        canvas.itemconfig(canvas_image, image=cardfront_image)
        canvas.itemconfig(lang_title, text="French", fill="black")
        canvas.itemconfig(word_title, text=choosen_card["French"], fill="black")
        flip_timer = window.after(3000, func=flip_card)
    except IndexError:
        game_end()


def flip_card():
    canvas.itemconfig(lang_title, text="English", fill="white")
    canvas.itemconfig(word_title, text=choosen_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=cardback_image)


def game_end():
    canvas.itemconfig(canvas_image, image=cardfront_image)
    canvas.itemconfig(lang_title, text="List finished!", fill="green")
    canvas.itemconfig(word_title, text="Reopen the game to reset!", fill="green", font=("Ariel", 40, "bold"))
    false_button.config(command="")
    true_button.config(command="")


# Known words button function

def known_words():
    try:
        data_dict.remove(choosen_card)
        pandas.DataFrame(data_dict).to_csv("data/words_to_learn.csv", index=False)
        new_card()
    except IndexError:
        game_end()


# UI codes

window = Tk()
window.title("Flashy Cards")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=flip_card)

cardback_image = PhotoImage(file="images/card_back.png")
cardfront_image = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 300, image=cardfront_image)
canvas.grid(row=0, column=0, columnspan=2)
lang_title = canvas.create_text(400, 150, text="LANG_TITLE", font=LANG_FONT)
word_title = canvas.create_text(400, 263, text="WORD", font=WORD_FONT)

true_image = PhotoImage(file="images/right.png")
false_image = PhotoImage(file="images/wrong.png")

false_button = Button(image=false_image, highlightthickness=0, command=new_card)
false_button.grid(row=1, column=0)

true_button = Button(image=true_image, highlightthickness=0, command=known_words)
true_button.grid(row=1, column=1)


new_card()

window.mainloop()
