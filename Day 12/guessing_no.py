import random
from guessing_art import logo
print(logo)
print("Welcome to the Number Guessing Game!!!")
number_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
           71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
           91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]
print("I am thinking the number between 1 and 100")
number = random.choice(number_list)
print(number)
choice = input("Choose the level of difficulty you want.Type 'easy' or 'hard': ").lower()
if choice == "easy":
    lives = 5
    flag = True
    while flag:
        print(f"You have {lives} out of 5 attempts left")
        guess = int(input("Make a guess of your choice: "))

        if guess == number:
            print("Congratulations!!! You have guessed it")
            flag = False
        elif guess > number:
            lives -= 1
            if lives == 0:
                print("You have {lives} out of 5 attempts left.")
                print("You Lose!!!")
                print(f"The correct number is {number}")
                flag = False
            else:
                print("Too high")
                print("Guess again")
                flag = True

        elif guess < number:
            lives -= 1
            if lives == 0:
                print("You have {lives} out of 5 attempts left.")
                print("You Lose!!!")
                print(f"The correct number is {number}")
                flag = False
            else:
                print("Too low")
                print("Guess again")
                flag = True
        else:
            lives -= 1
            if lives == 0:
                print("You have {lives} out of 5 attempts left.")
                print("You Lose!!!")
                print(f"The correct number is {number}")
                flag = False
            else:
                print("You have chosen the invalid guess")
                print("Guess again")
                flag = True
else:
    lives = 10
    flag = True
    while flag:
        print(f"You have {lives} out of 5 attempts left")
        guess = int(input("Make a guess of your choice: "))

        if guess == number:
            print("Congratulations!!! You have guessed it")
            flag = False
        elif guess > number:
            lives -= 1
            if lives == 0:
                print("You have {lives} out of 5 attempts left.")
                print("You Lose!!!")
                print(f"The correct number is {number}")
                flag = False
            else:
                print("Too high")
                print("Guess again")
                flag = True

        elif guess < number:
            lives -= 1
            if lives == 0:
                print("You have {lives} out of 5 attempts left.")
                print("You Lose!!!")
                print(f"The correct number is {number}")
                flag = False
            else:
                print("Too low")
                print("Guess again")
                flag = True
        else:
            lives -= 1
            if lives == 0:
                print("You have {lives} out of 5 attempts left.")
                print("You Lose!!!")
                print(f"The correct number is {number}")
                flag = False
            else:
                print("You have chosen the invalid guess")
                print("Guess again")
                flag = True