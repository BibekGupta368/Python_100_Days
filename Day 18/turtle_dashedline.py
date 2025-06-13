from turtle import Turtle,Screen
timmy = Turtle()
my_screen = Screen()

for i in range(15):  #0-14 ie 15 times
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

my_screen.exitonclick()

    
