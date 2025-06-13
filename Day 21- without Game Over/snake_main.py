from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
my_screen = Screen()
my_screen.setup(width = 500, height = 500)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)  #Turn off the tracer ie animation ofthe turtle

my_snake = Snake() #calling the class Snake
food = Food() #Calling the Food class that is inherited from the Turtle class
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(my_snake.left , "Left")   
my_screen.onkey(my_snake.right , "Right") 
my_screen.onkey(my_snake.up, "Up") 
my_screen.onkey(my_snake.down , "Down") 
flag = True
while flag:

    my_screen.update()  #Show the current animation of turtle
    time.sleep(0.1)
    my_snake.move()

    #Check whether it collide with the food
    if my_snake.head.distance(food) < 15: #Indicates the collision between the snake first block and the food
        food.refresh_position()
        my_snake.extend()
        scoreboard.increase_score()
    
    #Check whether it collide with the wall
    if my_snake.head.xcor() > 230 or my_snake.head.xcor() < -230 or my_snake.head.ycor() > 230 or my_snake.head.ycor() < -230:
        scoreboard.reset()
        my_snake.reset()

        
    
    #Check whether it collide with the tail
    
    """
    for block in my_snake.all_blocks:
        if block == my_snake.head:         #First block is the head of the snake ie distance between the head to head is always less than 10 ,so we have to pass it,otherwise initially the game get over.
            pass
        elif my_snake.head.distance(block) < 10:
            scoreboard.game_over()
            flag = False
    """

    #--------------or---------------------------#
    #--------------or---------------------------#

    for block in my_snake.all_blocks[1:]:      #Here we have used the concept of slicing list inorder to slice(skip) the 1st turtle ie head of the snake
        if my_snake.head.distance(block) < 10:
            scoreboard.reset()
            my_snake.reset()
           


   
my_screen.exitonclick()