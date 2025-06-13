from tkinter import *
from tkinter import messagebox
import random
import pandas

B_C = "#B1DDC6"
window = Tk()
window.title("Flash Card")
window.config(padx = 40,pady = 40,bg = B_C)

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg = B_C)
front_img = PhotoImage(file="Day 31/Capston Project/images/card_front.png")
back_img = PhotoImage(file="Day 31/Capston Project/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title =canvas.create_text(400, 155, text="Title", font=("Arial", 40, "bold"))
card_word =canvas.create_text(400, 263, text="Word", font=("Arial", 50, "italic"))
canvas.grid(column =0, row=0,columnspan = 2)     #Grid is divided into 2 rows and 2 columns

data_dict_list ={}
current_dict_card = {}
try:
    data = pandas.read_csv("Day 31/Capston Project/unknown_words.csv")
except (FileNotFoundError,pandas.errors.EmptyDataError):

    original_data = pandas.read_csv("Day 31/Capston Project/french_words.csv")   #store the data in Table format.
    data_dict_list = original_data.to_dict(orient = "records")  # Convert the data in table format to the list of dictionaries having each row in each dictionary.
else:
    data_dict_list = data.to_dict(orient = "records")

def next_card():
    global current_dict_card,flip_card_timer
    window.after_cancel(flip_card_timer)
    current_dict_card = random.choice(data_dict_list)
    canvas.itemconfig(card_title, text= "French",fill = "black")
    canvas.itemconfig(card_word, text= current_dict_card["French"], fill = "black")

    #calling the flip function after 3s
    flip_card_timer = window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image = back_img)
    canvas.itemconfig(card_title, text= "English", fill = "white")
    canvas.itemconfig(card_word, text= current_dict_card["English"], fill ="white")
def known_word():
    data_dict_list.remove(current_dict_card)
    data = pandas.DataFrame(data_dict_list)
    data.to_csv("Day 31/Capston Project/unknown_words.csv", index = False) #index = False, to avoid the index number otherwise each time a new index number will be there.
    next_card()

#Buttons
wrong_img = PhotoImage(file="Day 31/Capston Project/images/wrong.png")
wrong_button = Button(image =wrong_img,highlightthickness=0, command = next_card)
wrong_button.grid(column = 0, row = 1)

right_img = PhotoImage(file="Day 31/Capston Project/images/right.png")
right_button = Button(image = right_img,highlightthickness=0, command = known_word)
right_button.grid(column = 1, row = 1)

flip_card_timer = window.after(3000,flip_card)
next_card()


window.mainloop()