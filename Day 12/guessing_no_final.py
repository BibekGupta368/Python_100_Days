import random
from guessing_art import logo
def play_again():
    print(logo)
    print("Welcome to the Number Guessing Game!!!")
    print("I am thinking the number between 1 and 100.")

    number = random.randint(1, 100)                       #or from random2 import random_integer                                             
                                                          #  number = random_integer
    print(f"Just for my view. The answer is {number}.")

    def guessing(lives):
        
        flag = True
        while flag:
            print(f"You have {lives} attempts left to guess the number.")
            guess = int(input("Make a guess of your choice: "))

            if guess > number:
                lives -= 1
                if lives == 0:
                    print(f"You have {lives} attempts left.")
                    print("You Lose!!!")
                    print(f"The correct number was {number}.")
                    flag = False
                else:
                    print("Too high.")
                    print("Guess again. ")
                    flag = True

            elif guess < number:
                lives -= 1
                if lives == 0:
                    print(f"You have {lives} attempts left.")
                    print("You Lose!!!")
                    print(f"The correct number was {number}.")
                    flag = False
                else:
                    print("Too low.")
                    print("Guess again.")
                    flag = True
            else:          # guess == number:
                print(f"Congratulations!!! You have guessed it, the answer was {number}.")
                flag = False
    choice = input("Choose the level of difficulty you want.Type 'easy' or 'hard': ").lower()
    if choice == "easy":
        guessing(10)
    else: #choice == "hard":
        guessing(5)

flag1 = True
while flag1:
    prefer = input("Do you to want to play Number Guessing Game!!!.Type 'yes' or 'quit': ").lower()
    if prefer == "yes":
        print("\n"*30)
        play_again()
        flag1 = True
    else:
        flag1 = False