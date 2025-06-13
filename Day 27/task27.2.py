# #------------------------------1st using pack()---------------------------------------------------------
# from tkinter import *
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width = 500, height = 300)
# #Label
# my_label = Label(text = "I am a Label", font = ("Arial", 20, "bold"))
# my_label.pack()   #Display the text at the top center bydefault

# #Changing the my_label original text to new text
# my_label["text"] = "New Text"   # or my_label.config(text = "New Text")

# def button_clicked():
#     print("I got clicked")

# #Button Creation
# button = Button(text = "Click Me", command =button_clicked)   
# button.pack()   #Display the button text at the top center bydefault

# window.mainloop()





# #-----------------------------2nd using pack()-------------------------------------------------
# from tkinter import *
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width = 500, height = 300)
# #Label
# my_label = Label(text = "I am a Label", font = ("Arial", 20, "bold"))
# my_label.pack()   #Display the text at the top center bydefault

# #Changing the my_label original text to new text
# my_label["text"] = "New Text"   # or my_label.config(text = "New Text")

# def button_clicked():
#     print("I got clicked") 
#     my_label["text"] = "Button got clicked"
   
# #Button Creation
# button = Button(text = "Click Me", command =button_clicked)   
# button.pack()   #Display the button text at the top center bydefault

# window.mainloop()





# #---------------------------------3rd using pack()----------------------------------------------------
# from tkinter import *
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width = 500, height = 300)
# #Label
# my_label = Label(text = "I am a Label", font = ("Arial", 20, "bold"))
# my_label.pack()   #Display the text at the top center bydefault

# #Changing the my_label original text to new text
# my_label["text"] = "New Text"   # or my_label.config(text = "New Text")

# def button_clicked():
#     print("I got clicked") 
#     new_text = input.get()   #Hold the input values
#     my_label["text"] = new_text
   
# #Button Creation
# button = Button(text = "Click Me", command =button_clicked)   
# button.pack()   #Display the button text at the top center bydefault

# #Entry
# input = Entry(width = 10)
# input.pack()    #Display the input box at the top center bydefault

# window.mainloop()






# #---------------------------------4th using place()----------------------------------------------------
# from tkinter import *
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width = 500, height = 300)
# #Label
# my_label = Label(text = "I am a Label", font = ("Arial", 20, "bold"))
# my_label.place(x=100, y=0)    #Display the text at the given coordinates

# #Changing the my_label original text to new text
# my_label["text"] = "New Text"   # or my_label.config(text = "New Text")

# def button_clicked():
#     print("I got clicked") 
#     new_text = input.get()   #Hold the input values
#     my_label["text"] = new_text
   
# #Button Creation
# button = Button(text = "Click Me", command =button_clicked)   
# button.place(x=100, y=100)   #Display the button text at the given coordinates


# #Entry
# input = Entry(width = 10)
# input.place(x=100, y=200)    #Display the input box at the given coordinates
 
# window.mainloop()





# #---------------------------------5th using grid()----------------------------------------------------
# from tkinter import *
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width = 500, height = 300)
# #Label
# my_label = Label(text = "I am a Label", font = ("Arial", 20, "bold"))
# my_label.grid(column=0, row=0)    #Display the text at the given grid

# #Changing the my_label original text to new text
# my_label["text"] = "New Text"   # or my_label.config(text = "New Text")

# def button_clicked():
#     print("I got clicked") 
#     new_text = input.get()   #Hold the input values
#     my_label["text"] = new_text
   
# #Button Creation
# button = Button(text = "Click Me", command =button_clicked)   
# button.grid(column=1, row=1)   #Display the button text at the given grid

# #Entry
# input = Entry(width = 10)
# input.grid(column=2, row=2)    #Display the input box at the given grid

# window.mainloop()





#---------------------------------6th using grid()----------------------------------------------------
from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300)
window.config(padx=100, pady=100)     #Created the spaces around the window

#Label
my_label = Label(text = "I am a Label", font = ("Arial", 20, "bold"))
my_label.grid(column=0, row=0)   #Display the text at the given grid

#Changing the my_label original text to new text
my_label["text"] = "New Text"   # or my_label.config(text = "New Text")

def button_clicked():
    print("I got clicked") 
    new_text = input.get()   #Hold the input values
    my_label["text"] = new_text
   
#Button Creation
button = Button(text = "Click Me", command =button_clicked)   
button.grid(column=1, row=1)  #Display the button text at the given grid

#New Button Creation
new_button = Button(text = "New Button")   
new_button.grid(column=2, row=0)  

#Entry
input = Entry(width = 10)
input.grid(column=3, row=2)   #Display the input box at the given grid

window.mainloop()