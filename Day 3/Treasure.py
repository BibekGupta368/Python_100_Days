#https://ascii.co.uk/art#google_vignette Ctrl + f to saerch
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")
#choice1 = input("You're at a cross road!!Where you want to go?Type 'left' or 'right'.\n").lower() ##.lower()->return a copy of string converted to a lowercase
choice1 = input('You\'re at a cross road!!Where you want to go?Type "left" or "right".\n').lower()
if choice1 == "left":
    print("You've come to a lake.There is a island in the middle of the lake.")
    choice2 = input("What you want to choose?Type 'wait' to wait for boat and 'swim' to swim across\n").lower()
    if choice2 == "wait":
        print("You've arrived at the island.")
        choice3 = input("There is a house with 3 doors,one red,one blue and one yellow.Which one will you choose?'red','blue' or 'yellow'\n").lower()
        if choice3 == "red":
            print("Burned by the Fire.Game Over!!!")
        elif choice3 == "blue":
            print("Eaten by the beasts.Game Over!!!")
        elif choice3 == "yellow":
            print("You found the Treasure.Congratulation You Win!!!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.Game Over!!!")    
else:
    print("You fall into a hole.Game Over!!!")

