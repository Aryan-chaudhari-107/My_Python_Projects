from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- GENERATE RANDOM WORD ------------------------------- #
data = pandas.read_csv("data/hindi_words.csv")
words_dict = data.to_dict(orient="records")


# ---------------------------- ACTIVATE BUTTON ------------------------------- #
def next_card():
    current_word = random.choice(words_dict)
    canvas.itemconfig(card_title, text="Hindi")
    canvas.itemconfig(card_word, text= current_word["Hindi"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 130, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# WRONG BUTTON
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

# RIGHT BUTTON
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

next_card()






window.mainloop()