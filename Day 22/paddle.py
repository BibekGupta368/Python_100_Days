from turtle import Turtle
MOVED_DISTANCE = 20
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()       #Call the initialiser in the Turtle class where the turtle ie food is created that is happened inside the Turtle class  as self.new = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  #Dimension of paddle is height is 100 and width is 20
        self.penup() 
        self.goto(position)

    def up(self):
        new_y = self.ycor() + MOVED_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVED_DISTANCE
        self.goto(self.xcor(), new_y)
