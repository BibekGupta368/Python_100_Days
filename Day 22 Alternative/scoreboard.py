from turtle import Turtle    #Importing the class Turtle from turtle.py

class ScoreBoard(Turtle):
    def __init__(self,position):
        super().__init__()  #Call the initialiser in the Turtle class where the turtle is created that is happened inside the Turtle class as self.new = Turtle() Which is extra here and can be created in the shape of arrow so we have to hide it.
        self.score = 0
        self.color("white") #Default color is black so inorder to see it we have to set it to white
        self.penup()
        self.hideturtle() 
        self.update_score(position)

    def update_score(self,position):
        self.goto(position)
        self.write(f"Score : {self.score}", align = "center",font = ("Arial",18,"normal"))  # write this text where the turtle is located currently so inorder to keep it in the desired place,first move the turtle to that place and then write this line. 

    def l_point_increase(self):
        self.score +=1
        self.clear()
        self.update_score((-100,250))
    
    def r_point_increase(self):
        self.score +=1
        self.clear()
        self.update_score((100,250))
    
