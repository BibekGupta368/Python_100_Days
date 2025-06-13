from turtle import Turtle   #Importing the class Turtle from turtle.py
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()     #Call the initialiser in the Turtle class where the turtle ie food is created that is happened inside the Turtle class  as self.new = Turtle()
        self.shape("circle")
        self.shapesize(stretch_wid= 1, stretch_len=1)  #Dimension of the ball is 20*20 pixel
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def move(self):
        xcor = self.xcor() + self.x_move
        ycor = self.ycor() + self.y_move
        self.goto(x = xcor, y= ycor)
    
    def bounce_from_y_cor(self):
        self.y_move *= -1    

    def bounce_from_paddle_x_cor(self):
        self.x_move *= -1    
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(x= 0,y = 0) 
        self.move_speed = 0.1
        self.bounce_from_paddle_x_cor()
