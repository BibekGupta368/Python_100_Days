from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25               # All th time in constants is in minutes
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reccur = 0   #reccurence
timer = None

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day 28- Pomodoro timer/tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 127, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column =4, row=4)

title_label = Label(text = "Timer",font = (FONT_NAME, 30, "bold"),fg =GREEN,bg =YELLOW)
title_label.grid(column =4, row=2)       #Grid is divided into 14 rows and 10 columns

checkmark_label = Label(font = (FONT_NAME, 10),fg =GREEN,bg =YELLOW)  
checkmark_label.grid(column =4, row=11)       #Grid is divided into 14 rows and 10 columns

def start_timer():
    global reccur    #After this line we can access the 'reccur' variable anywhere in the program with the value that is updated inside this function will be updated globally and can be used in another function too. 
    reccur += 1

    work_min = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reccur % 8 == 0:    #8
        title_label.config(text = "Break",fg = PINK)
        count_down(long_break_sec)
        
    if reccur % 2 == 0:    #2,4,6
        title_label.config(text = "Break",fg = PINK)
        count_down(short_break_sec)

    else:   #1,3,7
        title_label.config(text = "Work",fg = RED)
        count_down(work_min)
    
def count_down(count):
    global timer    #After this line we can access the 'timer' variable anywhere in the program with the value that is updated inside this function will be updated globally and can be used in another function too.
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}") 

    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        marks = ""
        work_sessions = math.floor(reccur/2)
        for i in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text = marks)
            
        start_timer()
    
def reset_timer():
    window.after_cancel(timer)   #To cancel or stop the timer
    canvas.itemconfig(timer_text, text = "00:00") 
    title_label.config(text = "Timer",fg = GREEN)
    checkmark_label.config(text = "" )
    global reccur
    reccur = 0      # To reset the 'reccur' value to 0

#Buttons Creation
start_button = Button(text = "Start", command =start_timer)   
start_button.grid(column=2, row=10)  #Display the button text at the given grid

reset_button = Button(text = "Reset", command =reset_timer)   
reset_button.grid(column=7, row=10)  #Display the button text at the given grid

window.mainloop()