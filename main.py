# Flash Card Project:

from tkinter import *

BACKGROUND = '#B1DDC6'

# ========================= Setup UI =============================
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND, highlightthickness=0)


# Canvas:
canvas = Canvas(width=800, height=526)
img = PhotoImage(file='./Flash-Card-Project/card_front.png')
canvas.create_image(400, 263,image=img)
canvas.grid(row=0, column=0)
canvas.config(bg=BACKGROUND, highlightthickness=0)
canvas.create_text(400, 150, text='Title', font=('Ariel', 36, 'italic'))
canvas.create_text(400, 280, text='Word', font=('Ariel', 56, 'bold'))


# Right button:
right_img = PhotoImage('Flash-Card-Project/wrong.png')
right_button = Button(image=right_img) 
right_button.grid(row=1, column=0)
right_button.config(height=100, width=100)



# ========================= Mechanism of Flash Card =============================
# ========================= Creating a new Flash Card =============================
# ========================= Fliping the Flash Card =============================
# ========================= Set timer =============================

window.mainloop()