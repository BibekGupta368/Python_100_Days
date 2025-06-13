from turtle import Turtle    #Importing the class Turtle from turtle.py

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()  #Call the initialiser in the Turtle class where the turtle is created that is happened inside the Turtle class as self.new = Turtle() Which is extra here and can be created in the shape of arrow so we have to hide it.
        self.score = 0

        with open("D:\Python 100 Days\Day 21- without Game Over\high_score.txt") as h_score:
            self.high_score = int(h_score.read())   #Here we needed int type so convert the string type to int type.
        
        self.color("white") #Default color is black so inorder to see it we have to set it to white
        self.penup()
        self.goto(x = 0, y = 220)
        self.update_score()
        self.hideturtle() 

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score = {self.high_score}", align = "center",font = ("Arial",18,"normal"))  # write this text where the turtle is located currently so inorder to keep it in the desired place,first move the turtle to that place and then write this line.

    def increase_score(self):
        self.score +=1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
            with open("D:\Python 100 Days\Day 21- without Game Over\high_score.txt",mode = "w") as h_score:
                h_score.write(f"{self.high_score}")
            
        self.score = 0
        self.update_score()
    
    # #Now we dont gonna end the game
    # def game_over(self):
    #     self.goto(x = 0, y = 0) #Moving the turtle to the center inorder to display the GAME OVER in the center 
    #     self.write(f"GAME OVER", align = "center",font = ("Arial",18,"normal"))
    
