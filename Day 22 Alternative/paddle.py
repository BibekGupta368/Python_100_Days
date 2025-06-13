from turtle import Turtle
POSITIONS = [(350,0),(-350,0)]
MOVED_DISTANCE = 20

class Paddle:
    def __init__(self):
        self.all_paddles =[]
        self.create_paddle()
        
    def create_paddle(self):
        
        for position in POSITIONS:
            new_paddle = Turtle(shape ="square")   #Dimension of the turtle is 20*20 pixel
            new_paddle.shapesize(stretch_wid= 5, stretch_len=1)  #Dimension of paddle is height is 100 and width is 20
            new_paddle.penup()
            new_paddle.color("white")
            new_paddle.goto(position)
            self.all_paddles.append(new_paddle)

    def up(self):
        new_y = self.all_paddles[0].ycor() + MOVED_DISTANCE
        self.all_paddles[0].goto(self.all_paddles[0].xcor(), new_y)

    def down(self):
        new_y = self.all_paddles[0].ycor() - MOVED_DISTANCE
        self.all_paddles[0].goto(self.all_paddles[0].xcor(), new_y)

    def up1(self):
        new_y = self.all_paddles[1].ycor() + MOVED_DISTANCE
        self.all_paddles[1].goto(self.all_paddles[1].xcor(), new_y)

    def down1(self):
        new_y = self.all_paddles[1].ycor() - MOVED_DISTANCE
        self.all_paddles[1].goto(self.all_paddles[1].xcor(), new_y)


    
    
