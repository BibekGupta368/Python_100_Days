from turtle import Turtle,Screen
import pandas
my_screen = Screen()
timmy = Turtle()
my_screen.title("U.S States Game")
my_screen.setup(725, 491)     # setup the width of the screen excatly as image

#Displaying the background of the screen as image
image = "Day 25\\US_states_game\\blank_states_img.gif"    #turtle only processes the .gif image format 
my_screen.addshape(image)
timmy.shape(image)   #Actually the timmy turtle shape now become a image

"""

#Getting the coordinates of each and every section on click but as the coordinates of every states is already given in the fifty_states.csv so don't need it here
def get_mouse_click_coor(x, y):
    print(x,y)
my_screen.onscreenclick(get_mouse_click_coor)  #When the mouse clicks on the screen ,it will calls the function and passes the x and y coordinates of that clicked section
my_screen.mainloop()                           #Keeps the screen open

"""

data = pandas.read_csv("Day 25/US_states_game/fifty_states.csv")
data["state"]
all_state_list = data["state"].to_list()  #converting the data of state to list

guessed_states = []
while len(guessed_states) < len(all_state_list):    #or while len(guessed_states) < 50:
    guess_state = my_screen.textinput(title = f"{len(guessed_states)}/50 Guess correct", prompt = "What is the state's name?").title()
    
    if guess_state == "Exit":
        """
        1st process of appending: Using For Loop
        missing_states = []
        for state in all_state_list:
            if state not in guessed_states:
                missing_states.append(state)
        """
        #2nd process using List comprehension:

        missing_states =[state for state in all_state_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states) 
        new_data.to_csv("Day 25/US_states_game/states_you_don't_know.csv")   #Created the new.csv file automatically       
        break
    if guess_state in all_state_list:
        tammy = Turtle()
        tammy.hideturtle()
        tammy.penup()
        guessed_state_row_data = data[data["state"] ==  guess_state]
        tammy.goto(guessed_state_row_data.x.item(), guessed_state_row_data.y.item())   #.item() because that way we'are accessing the single item contained in our panda series
        tammy.write(guess_state)      # or tammy.write(guessed_state_row_data.state.item()) 
        guessed_states.append(guess_state)


# my_screen.exitonclick()  #Don't needed it as we use exit to come out of the while Loop and until the while Loop runs the screen doesn't disappears.
