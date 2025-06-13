 if my_snake.head.xcor() > 230 or my_snake.head.xcor() < -230 or my_snake.head.ycor() > 230 or my_snake.head.ycor() < -230:
        scoreboard.game_over()
        flag = False
    