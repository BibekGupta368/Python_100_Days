import random
import hangman_words                   # or from hangman_words import word_list
from hangman_art import hangman_stages # or from hangman_art import hangman_stages,logo
from hangman_art import logo           # or import hangman_art
print(logo)                            # or print(hangman_art.logo)
lives = 6
chosen_word = random.choice(hangman_words.word_list)  # or chosen_word = random.choice(word_list)
placeholder = ''
word_length = len(chosen_word)
for letter in chosen_word:   # for i in range(word_length) or for i in range(0, word_length)
    placeholder += "_"
Hint = print(placeholder) 
correct_letters = []
game_over = False
while not game_over :
    print(f"{lives} out of 6 lives left")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed this letter : {guess}")
    display = '' 
    for letter in chosen_word:
        if guess == letter:
            display += guess
            correct_letters.append(guess) 

        elif letter in correct_letters:
            display += letter 
        else:
            display += "_" 
            
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} you have guessed is incorrect.You lose a life!!!")
        if lives == 0:
            game_over = True
            print(f"The correct word was {chosen_word}.You lose!!!")
            print("Game Over")
         
    if "_" not in display:
        game_over = True
        print("You win")
        print("Game Over")
    
    print(hangman_stages[6-lives])

   