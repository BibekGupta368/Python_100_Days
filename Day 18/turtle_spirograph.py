import random
import turtle as t 
timmy = t.Turtle()
my_screen = t.Screen()
t.colormode(255)
timmy.speed("fastest")
 
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)         #Created a tuple here with r,g and b
    return rgb_color 
 
def draw_spiro(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap) #shifting by the given degree(size_of_gap) each time.Here size_of_gap = 5 degree ,so it is shifting by 5 degree each time.

draw_spiro(10)
my_screen.exitonclick()


