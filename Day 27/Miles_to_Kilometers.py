from tkinter import *
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width = 200, height = 100)
window.config(padx=50, pady=25)     #Created the spaces around the window

#Label
miles_label = Label(text = "Miles")
miles_label.grid(column=3, row=1)      #Grid is divided into 5 rows and 4 columns

is_equal_to_label = Label(text = "is equal to")
is_equal_to_label.grid(column=1, row=2) 

km_label = Label(text = "Km")
km_label.grid(column=3, row=2) 

kilo_result_label = Label(text = "0")
kilo_result_label.grid(column=2, row=2) 

def calculate_miles_to_km():
    miles = float(input_miles.get())     #Hold the input values
    km = miles * 1.609                 # convert the miles to km
    kilo_result_label.config(text = km)  # or result_label["text"] = km 
   
#Button Creation
calculate_button = Button(text = "Calculate", command =calculate_miles_to_km)   
calculate_button.grid(column=2, row=3)  

#Entry
input_miles = Entry(width = 8)
input_miles.grid(column=2, row=1)

#Add some text to begin with
input_miles.insert(END, string="0")

#Puts cursor in input_miles box while executing.
input_miles.focus()

window.mainloop()