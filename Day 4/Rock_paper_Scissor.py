import random
choice = int(input("What do you choose?Type 0 or Rock,1 for Paper and 2 for Scissors\n"))
if choice == 0:
    print("You choose: Rock")                                  
    Rock = '''                                            
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''  
    print(Rock)     
elif choice == 1:
    print("You choose: Paper")
    Paper = '''
       _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
   
    '''  
    print(Paper)
elif choice == 2:
    print("You choose: Scissors")
    print('''
    ---  '____)____
              ______)
           __________)
          (____)
    ---.__(___)     
            
                   ''')
else:
    print("Invalid choice")

c_choice = random.randint(0, 2)
if c_choice == 0:
    print("Computer choose: Rock")
    Rock = '''                                            
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''  
    print(Rock)  
elif c_choice == 1:
    print("Computer Choose: Paper")
    Paper = '''
       _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
   
    '''  
    print(Paper)
else:
    print("Computer choose: Scissors")
    print('''
    ---  '____)____
              ______)
           __________)
          (____)
    ---.__(___)     
            
                   ''')
    
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

