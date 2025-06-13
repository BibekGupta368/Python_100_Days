#Drawing a 10*10 hirst painting with dots, so it include 100 dots in total
import random
import turtle as t
timmy = t.Turtle()
my_screen = t.Screen()
t.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

# This color list i have used from the project 1
actual_rgb_list =[(244, 229, 50), (202, 7, 33), (237, 228, 2), (193, 67, 24), (221, 151, 81), (36, 210, 91), (240, 41, 122), (35, 92, 177), (32, 31, 156), (205, 11, 5), (16, 18, 53), (92, 185, 218), (64, 9, 44), (231, 156, 6), (58, 21, 10), (206, 31, 94), (219, 134, 178), (12, 201, 221), (18, 149, 28), (90, 237, 168), (237, 58, 31), (81, 212, 150), (96, 75, 9), (238, 160, 199), (87, 87, 206), (6, 37, 28), (10, 96, 62), (90, 227, 239), (239, 170, 161), (253, 6, 21), (254, 7, 5)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

no_of_dots = 100
for dots_cnt in range(1, no_of_dots + 1):    #Runs for 1 to 100 ie 100 times ie 100 dots
    timmy.dot(20, random.choice(actual_rgb_list))
    timmy.forward(50)
    
    if dots_cnt % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

my_screen.exitonclick()