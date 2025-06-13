from turtle import Screen
from player import Player
from car import Car
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width = 600, height = 600)
my_screen.title("My Game")
my_screen.tracer(0)  #Turn off the tracer ie animation of the turtle

my_player = Player()
my_car = Car()
scoreboard = ScoreBoard()
my_screen.listen()

my_screen.onkey(my_player.move_up, "Up") 

flag = True
while flag:
    time.sleep(my_player.move_speed)
    my_screen.update()
    my_car.create_cars()
    my_car.move_cars()

    #Check Whether the turtle collides with the Car
    for car in my_car.all_cars:
        if my_player.distance(car) < 20:
            scoreboard.game_over()
            flag = False

    #Check whether the turtle has finished the cross line and go to next level
    if my_player.ycor() > 280:   #Y_FINISH_LINE = 280
        my_player.reset_position_for_next_lvl()
        scoreboard.increase_level()







my_screen.exitonclick()