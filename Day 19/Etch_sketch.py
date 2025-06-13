from turtle import Turtle,Screen
timmy = Turtle()
my_screen = Screen()

def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def counter_clockwise():
    # timmy.seth(270)
    timmy.left(90)
    timmy.left(90)
    timmy.left(90)

def clockwise():
    # timmy.seth(90)
    timmy.right(90)
    timmy.right(90)
    timmy.right(90)

def clear_screen():
    timmy.clear()    #or  timmy.clear() or timmy.reset()
    timmy.penup()
    timmy.home()
    timmy.pendown()

def undo():
    timmy.undo()

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.seth(new_heading)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.seth(new_heading)

    

my_screen.listen()
#Here,i have used the positional argument . You can also use the Keyword argument as in the comment
my_screen.onkey(move_forward , "f")   #or my_screen.onkey(fun = move_forward , key = "f") #or  my_screen.onkey( key = "f", fun = move_forward)
my_screen.onkey(move_backward, "b")
my_screen.onkey(counter_clockwise, "a")
my_screen.onkey(clockwise, "d")
my_screen.onkey(clear_screen, "c")
my_screen.onkey(undo, "z")
my_screen.onkey(turn_left, "l")
my_screen.onkey(turn_right, "r")

my_screen.exitonclick()
