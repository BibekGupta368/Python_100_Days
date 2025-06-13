from turtle import Turtle    #Importing the class Turtle from turtle.py

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()  #Call the initialiser in the Turtle class where the turtle is created that is happened inside the Turtle class as self.new = Turtle() Which is extra here and can be created in the shape of arrow so we have to hide it.
        self.level = 1
        self.color("Black") #Default color is black so inorder to see it we have to set it to white
        self.penup()
        self.goto(x = -250, y = 260)
        self.update_scoreboard()
        self.hideturtle() 
        
    def update_scoreboard(self):
        self.write(f"Level : {self.level}", align = "center",font = ("Arial",18,"normal"))  # write this text where the turtle is located currently so inorder to keep it in the desired place,first move the turtle to that place and then write this line.
        
    def increase_level(self):
        self.level +=1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(x = 0, y = 0) #Moving the turtle to the center inorder to display the GAME OVER in the center 
        self.write(f"GAME OVER", align = "center",font = ("Arial",18,"normal"))
