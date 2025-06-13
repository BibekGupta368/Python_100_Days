import random
Rock = '''                                            
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''  
Paper = '''
       _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
   
    ''' 
Scissors = '''

    ---  '____)____
              ______)
           __________)
          (____)
    ---.__(___)     
            
                   '''
game_images = [Rock, Paper, Scissors]
choice = int(input("What do you choose?Type 0 or Rock,1 for Paper and 2 for Scissors\n"))
if 0 <= choice <=2:
    print("You choose: " + game_images[choice])
    # print(game_images[choice])
else:
     print("Invalid choice")
c_choice = random.randint(0, 2)
print("Computer choose: " + game_images[c_choice])

if choice == c_choice:
    print("It's a Draw")
elif choice == 0 and c_choice == 1:
    print("You Lose")
elif choice == 0 and c_choice == 2:
    print("You won")
elif choice == 1 and c_choice == 0:
    print("You won")
elif choice == 1 and c_choice == 2:
    print("You Lose")
elif choice == 2 and c_choice == 0:
    print("You Lose")
elif choice == 2 and c_choice == 1:
    print("You won")
else:
    print("Invalid choice made by you !! ! You Lose")