# Flash Card Project:

from tkinter import *
import pandas as pd, random

BACKGROUND = '#B1DDC6'

current_card = {}
to_learn = {}

try:
    data = pd.read_csv('./Flash-Card-Project/words_learn.csv')
    
except FileNotFoundError:
    original_data = pd.read_csv('./Flash-Card-Project/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
    
else:
    to_learn = data.to_dict(orient='records')
                       
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=front_img)
    
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=back_img)
    
def is_learn():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('./Flash-Card-Project/words_learn.csv', index=False)
    
    next_card()


# ========================= Setup UI =============================
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND, highlightthickness=0)
flip_timer = window.after(3000, func=flip_card)

# Canvas:
canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file='./Flash-Card-Project/card_front.png')
back_img = PhotoImage(file='./Flash-Card-Project/card_back.png')
card_background = canvas.create_image(400, 263,image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND, highlightthickness=0)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 32, 'italic'))
card_word = canvas.create_text(400, 280, text='Word', font=('Ariel', 52, 'bold'))


# Right button:
right_img = PhotoImage(file='./Flash-Card-Project/right.png')
right_button = Button(image=right_img,command=is_learn) 
right_button.grid(row=1, column=1)
right_button.config(height=100, width=100, highlightthickness=0)


# Wrong button:
wrong_img = PhotoImage(file='./Flash-Card-Project/wrong.png')
wrong_button = Button(image=wrong_img,command=next_card) 
wrong_button.grid(row=1, column=0)
wrong_button.config(height=100, width=100, highlightthickness=0)

next_card()

window.mainloop()