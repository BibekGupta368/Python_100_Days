# #1st method

# from turtle import Turtle,Screen
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")

# #Drawing a Triangle
# for i in range(3):
#     timmy.forward(100)
#     timmy.right(120)

# #Drawing a Square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
    
# #Drawing a Pentagon
# for i in range(5):
#     timmy.forward(100)
#     timmy.right(72)

# #Drawing a Hexagon
# for i in range(6):
#     timmy.forward(100)
#     timmy.right(60)

# #Drawing a Heptagon
# for i in range(7):
#     timmy.forward(100)
#     timmy.right(51.43)

# #Drawing a Octagon
# for i in range(8):
#     timmy.forward(100)
#     timmy.right(45)

# #Drawing a Nonagon
# for i in range(9):
#     timmy.forward(100)
#     timmy.right(40)

# #Drawing a Pentagon
# for i in range(10):
#     timmy.forward(100)
#     timmy.right(36)

# my_screen.exitonclick()




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


