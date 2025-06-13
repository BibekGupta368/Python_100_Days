#2nd method
import random
import turtle as t
timmy = t.Turtle()
my_screen = t.Screen()
colors = ["DarkBlue", "	DarkGreen", "Purple", "MediumOrchid"]

def draw_shape(sides):
    timmy.color(random.choice(colors))
    angle = 360 / sides
    for i in range(sides):
        timmy.forward(100)
        timmy.right(angle)

for j in range(3,11):  #runs from 3 to 10
    # timmy.color(random.choice(colors))
    draw_shape(j)

my_screen.exitonclick()