from turtle import Turtle
INITIAL_STARTING_POS = (0, -280)
UP = 90
DISTANCE_MOVED = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()   #Call the initialiser in the Turtle class where the turtle ie food is created that is happened inside the Turtle class  as self.new = Turtle()
        self.shape("turtle")
        self.penup()
        self.goto(INITIAL_STARTING_POS)
        self.seth(UP)
        self.move_speed = 0.1

    def move_up(self):
        self.forward(DISTANCE_MOVED)
    
    def reset_position_for_next_lvl(self):
        self.goto(INITIAL_STARTING_POS)
        self.move_speed *= 0.4


