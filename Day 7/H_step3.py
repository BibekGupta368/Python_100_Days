import random
word_list = ['epidemic', 'baboon', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ''
word_length = len(chosen_word)
for letter in chosen_word:   # for i in range(word_length) or for i in range(0, word_length)
    placeholder += "_"
Hint = print(placeholder) 
correct_letters = []
game_over = False
while not game_over :
    guess = input("Guess a letter: ").lower()
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
    if "_" not in display:
        game_over = True
        print("You win")


  