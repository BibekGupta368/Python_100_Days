from turtle import Turtle,Screen
import random
my_screen = Screen()

#Set the dimension of the screen
my_screen.setup(width = 500, height = 400)

#Dialog Window
choice_bet = my_screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter your color: ")

colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_coordinate = [-80, -50, -20, 10, 40, 70]
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle("turtle")    #or  new_turtle = Turtle(shape = "turtle")  or #new_turtle = Turtle()
                                                                                    #new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y_coordinate[i])
    all_turtles.append(new_turtle)

flag = True
while flag:
    for turtle in all_turtles:
        if flag == True:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()    #Gives the body color of turtle
                if winning_color == choice_bet:
                    print(f"You've won the bet.The {winning_color} turtle is the winner!!! ")
                else:
                    print(f"You've lost the bet.The {winning_color} turtle is the winner!!! ")

                flag = False
            else:
                turtle.forward(random.randint(0, 10))

my_screen.exitonclick()
