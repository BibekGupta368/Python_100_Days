# #1st method

# import random
# from turtle import Turtle,Screen
# timmy = Turtle()
# my_screen = Screen()
# # colors = ["DarkBlue", "Purple", "MediumOrchid,"CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue","LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# colors = ["DarkBlue", "Purple", "MediumOrchid", "CornflowerBlue", "DarkOrchid", "IndianRed", 
#           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]



# directions = [0, 90, 180, 270]
# timmy.width(15)  #timmy.pensize(15)
# timmy.speed("fastest")

 
# for i in range(200):

#     timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# my_screen.exitonclick()

"""--------------------------------------------------------------------------------------------------------"""

# #2nd method by generating random RGB

# import random
# from turtle import Turtle,Screen,colormode
# timmy = Turtle()
# my_screen = Screen()
# colormode(255)

# directions = [0, 90, 180, 270]
# timmy.width(15)  #timmy.pensize(15)
# timmy.speed("fastest")

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color 
 
# for i in range(200):

#     timmy.color( random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
# my_screen.exitonclick()

"""--------------------------------------------------------------------------------------------------------------------------"""

#3rd method by generating random RGB and another importing process

import random
import turtle as t 
timmy = t.Turtle()
my_screen = t.Screen()
t.colormode(255)

directions = [0, 90, 180, 270]
timmy.width(15)  #timmy.pensize(15)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)         #Created a tuple here with r,g and b
    return rgb_color 
 
for i in range(200):

    timmy.color( random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
my_screen.exitonclick()


