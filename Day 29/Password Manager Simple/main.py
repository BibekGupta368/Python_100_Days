from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

canvas = Canvas(width=200, height=189, highlightthickness=0)
lock_img = PhotoImage(file="Day 29/Password Manager Simple/password_logo.png")
canvas.create_image(100, 85, image=lock_img)
canvas.grid(column =1, row=5)     #Grid is divided into 15 rows and 3 columns

def data_adding():
    website_input_data = website_input.get()
    email_input_data = email_input.get()
    password_input_data = password_input.get()
    
    if len(website_input_data) == 0 or len(email_input_data) == 0 or len(password_input_data) == 0:
        messagebox.showinfo(title = "Oops", message="Don't leave any field empty")
    else:
        message_response_is_ok = messagebox.askokcancel(title = website_input_data,message = f"These are the details entered\nEmail: {email_input_data}\nPassword: {password_input_data}\nIs it ok to save?")

        if message_response_is_ok :
            messagebox.showinfo(title = "Success", message=f"Added {website_input_data} to the Data store")
            with open("Day 29/Password Manager Simple/data.txt",mode = "a") as data_file:
                data_file.write(f"{website_input_data } | {email_input_data} | {password_input_data}\n")
                website_input.delete(0,END)
                email_input.delete(0,END)
                password_input.delete(0,END)
        
        else:
            website_input.delete(0,END)
            email_input.delete(0,END)
            password_input.delete(0,END)

def generator_generate():

    password_input.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    n_letters = random.randint(9,12)
    n_symbols = random.randint(3,5)
    n_numbers = random.randint(3,5)

    
    password_letters = [random.choice(letters) for i in range(1, n_letters + 1)]
        
    password_symbols = [random.choice(symbols) for j in range(1, n_symbols + 1)]   

    password_numbers = [random.choice(numbers) for k in range(1, n_numbers + 1)]
    password_list =password_letters + password_symbols + password_numbers
    
    random.shuffle(password_list)

    password = "".join(password_list)   #Converts list into string

    password_input.insert(0, string = password)

    pyperclip.copy(password)   #Copied the password to the clipboard
    
#Labels
website_label = Label(text ="Website:")
website_label.grid(column =0, row=8)

email_label = Label(text ="Email/Username:")
email_label.grid(column =0, row=9)

password_label = Label(text ="Password:")
password_label.grid(column =0, row=10)

#Entries
website_input = Entry(width = 52)
website_input.grid(column=1, row=8,columnspan = 2) 
website_input.focus()

email_input = Entry(width = 52)
email_input.grid(column=1, row=9,columnspan = 2) 
# email_input.insert(0, string="bibekgupta2892@gmail.com")

password_input = Entry(width = 33)
password_input.grid(column=1, row=10) 

#Buttons
generate_password_button = Button(text = "Generate Password",width =15,command =generator_generate)
generate_password_button.grid(column=2, row=10)

add_button = Button(text = "Add",width =44,command = data_adding)
add_button.grid(column=1, row=11,columnspan = 2)

window.mainloop()





