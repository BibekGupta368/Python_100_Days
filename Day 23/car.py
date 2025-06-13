from turtle import Turtle 
import random
colors = ["red", "orange", "yellow", "blue", "purple", "green"]

class Car:
    def __init__(self):
        self.all_cars =[]

    def create_cars(self):
        random_number = random.randint(1,6)
        if random_number == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  #Dimension of the ball is 20*40 pixel
            new_car.color(random.choice(colors))
            new_car.penup()
            random_y = random.randint(-250,250)        #Upper 50 and lower 50 can be considered as the safe zone for turtle
            new_car.goto(x = 300, y = random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(5)

