from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width = 800, height = 600)
my_screen.bgcolor("black")
my_screen.title("My Pong Game")
my_screen.tracer(0)  #Turn off the tracer ie animation of the turtle

my_paddle = Paddle() 

my_screen.listen()

my_screen.onkey(my_paddle.up, "Up") 
my_screen.onkey(my_paddle.down , "Down") 
my_screen.onkey(my_paddle.up1, "w") 
my_screen.onkey(my_paddle.down1 , "s") 

my_ball = Ball()

left_score = ScoreBoard((-100,250))
right_score = ScoreBoard((100,250))

flag = True
while flag:
    time.sleep(my_ball.move_speed)
    my_screen.update()  #Show the current animation of turtle #update the screen and show us that has happened so far.

    my_ball.move()

    #Detecting whether it collide with the wall of y coordinate ie top and bottom wall because in x coordinate there is a paddle
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_from_y_cor()
    
    #Detecting whether it collide with the paddle 
    if my_ball.distance(my_paddle.all_paddles[0]) < 50  and my_ball.xcor() > 320 or my_ball.distance(my_paddle.all_paddles[1]) < 50 and my_ball.xcor() < -320:
        my_ball.bounce_from_paddle_x_cor()

    #Detecting whether the right paddle misses the ball
    if my_ball.xcor() > 380:
        my_ball.reset_position()
        left_score.l_point_increase()

    #Detecting whether the left paddle misses the ball
    if my_ball.xcor() < -380:
        my_ball.reset_position()
        right_score.r_point_increase()

my_screen.exitonclick()