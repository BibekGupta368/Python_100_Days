from turtle import Turtle
POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVED_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270
class Snake:
    def __init__(self):
        self.all_blocks =[]
        self.create_snake()
        self.head = self.all_blocks[0]  #store the head of the snake ie the first block
    
    def create_snake(self):
        
        for position in POSITIONS:
            self.add_new_block(position)
    
    def add_new_block(self,position):

            new_block = Turtle(shape ="square")   #Dimension of the turtle is 20*20 pixel
            new_block.penup()
            new_block.color("white")
            new_block.goto(position)
            self.all_blocks.append(new_block)

    def extend(self):
        self.add_new_block(self.all_blocks[-1].position())

    def move(self):
        for block_num in range(len(self.all_blocks)-1,0,-1):  #(2, 0, -1)
            new_x = self.all_blocks[block_num -1].xcor()
            new_y = self.all_blocks[block_num -1].ycor()
            self.all_blocks[block_num].goto(new_x,new_y)
        self.head.forward(MOVED_DISTANCE)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  #setheading(-90)
    
