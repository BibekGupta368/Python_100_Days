# # 1st Topic : Object and class
# # import turtle
# # timmy = turtle.Turtle()
# # print(timmy)

# """OR"""
# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)


# #2nd Topic: Object Attribute
# from turtle import Screen
# my_screen = Screen()
# print(my_screen.canvheight)


# #3rd Topic: Object Method
# from turtle import Screen
# my_screen = Screen()
# my_screen.exitonclick()


# #Topic 4 : Combining all the 3 examples
# # from turtle import Turtle,Screen
# # timmy = Turtle()
# # print(timmy)
# # my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()

# """OR"""

# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")     #Changes the shape from arrow to Turtle
# timmy.color("chartreuse") #Changes the color ffrom black to chartreuse color
# timmy.forward(100)        #Moves the Turtle forwrad by distance 100
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# #Topic 5
# from prettytable import PrettyTable
# table = PrettyTable()
# print(table)



# #Topic 6
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon",["Pikachu", "Charlizard", "Squirtel"])
# table.add_column("Type",["Electric", "Fire", "Water"])
# # table.align = "l"
# # table.align = "r"
# # table.align = "c"  #By default the computer choose this
# print(table.align)
# print(table)




