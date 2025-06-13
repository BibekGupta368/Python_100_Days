from turtle import Turtle   #Importing the class Turtle from turtle.py
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()     #Call the initialiser in the Turtle class where the turtle ie food is created that is happened inside the Turtle class  as self.new = Turtle()
        self.shape("circle")
        self.shapesize(stretch_wid= 0.5, stretch_len=0.5)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.refresh_position()
    
    def refresh_position(self):
        xcor = random.randint(-230, 230)
        ycor = random.randint(-230, 230)
        self.goto(x = xcor, y= ycor)