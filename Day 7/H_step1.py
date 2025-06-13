import random
word_list = ['epidemic', 'baboon', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")