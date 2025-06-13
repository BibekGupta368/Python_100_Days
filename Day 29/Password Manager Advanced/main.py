from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

canvas = Canvas(width=200, height=189, highlightthickness=0)
lock_img = PhotoImage(file="Day 29/Password Manager Advanced/password_logo.png")
canvas.create_image(100, 85, image=lock_img)
canvas.grid(column =1, row=5)     #Grid is divided into 15 rows and 3 columns

def data_adding():
    website_input_data = website_input.get()
    email_input_data = email_input.get()
    password_input_data = password_input.get()

    new_data = {
        website_input_data: {
            "email":email_input_data,
            "password":password_input_data
        }
    }
    
    if len(website_input_data) == 0 or len(email_input_data) == 0 or len(password_input_data) == 0:
        messagebox.showinfo(title = "Oops", message="Don't leave any field empty")
    else:
        message_response_is_ok = messagebox.askokcancel(title = website_input_data,message = f"These are the details entered\nEmail: {email_input_data}\nPassword: {password_input_data}\nIs it ok to save?")

        if message_response_is_ok :
            messagebox.showinfo(title = "Success", message=f"Added {website_input_data} to the Data store")
            
            try:
                with open("Day 29/Password Manager Advanced/data.json", "r") as data_file:   #If the data.json file doesn't exits then it will produce FileNotFoundError,so we have to use event handling to overcome this issue and go to except section.

                    #Reading the previous datas
                    data = json.load(data_file)   #If the data.json file exists and is initially empty then it will load nothing and produce an error(json.decoder.JSONDecodeError) ,so we have to use event handling to overcome this issue and go to except section.
                                                  
            except (FileNotFoundError , json.decoder.JSONDecodeError):
                with open("Day 29/Password Manager Advanced/data.json", "w") as data_file:
                    json.dump(new_data, data_file , indent=4)

            else:
                #Updating the old datas along with the new datas
                data.update(new_data)
                with open("Day 29/Password Manager Advanced/data.json", "w") as data_file:
                    #Saving the updated data in file
                    json.dump(data, data_file , indent=4)

            finally:
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

def find_password():
    website_input_data =website_input.get()
    try:
        with open("Day 29/Password Manager Advanced/data.json", "r") as data_file:      #If the data.json file doesn't exits then it will produce FileNotFoundError,so we have to use event handling to overcome this issue and go to except section.
 
            #Reading the previous datas
            data = json.load(data_file)   #It holds the list of dictionaries   #If the data.json file exists and is initially empty then it will load nothing and produce an error(json.decoder.JSONDecodeError) ,so we have to use event handling to overcome this issue and go to except section.

    except (FileNotFoundError, json.decoder.JSONDecodeError ):
        messagebox.showinfo(title = "Error!!!", message="Data file missing!!! ")
        
    else:
        if website_input_data in data:
            website_email = data[website_input_data]["email"]
            website_password = data[website_input_data]["password"]
            messagebox.showinfo(title = website_input_data, message=f"Email: {website_email} \n Password: {website_password}")

        else:
            messagebox.showinfo(title = "Error!!!", message=f"No data found for {website_input_data} in the record")
    
    
#Labels
website_label = Label(text ="Website:")
website_label.grid(column =0, row=8)

email_label = Label(text ="Email/Username:")
email_label.grid(column =0, row=9)

password_label = Label(text ="Password:")
password_label.grid(column =0, row=10)

#Entries
website_input = Entry(width = 33)
website_input.grid(column=1, row=8) 
website_input.focus()

email_input = Entry(width = 52)
email_input.grid(column=1, row=9,columnspan = 2) 
# email_input.insert(0, string="bibekgupta2892@gmail.com")

password_input = Entry(width = 33)
password_input.grid(column=1, row=10) 

#Buttons
search_button = Button(text = "Search",width =15,command =find_password)
search_button.grid(column=2, row=8)

generate_password_button = Button(text = "Generate Password",width =15,command =generator_generate)
generate_password_button.grid(column=2, row=10)

add_button = Button(text = "Add",width =44,command = data_adding)
add_button.grid(column=1, row=11,columnspan = 2)

window.mainloop()





