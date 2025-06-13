import random
from blackjack_art import logo
def dealer_cards():
    cards_list = [10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 11]
    card_choice = random.choice(cards_list)
    return card_choice

def calculate_score(cards):

    if len(cards) == 2 and sum(cards) == 21:    # or if len(cards) == 2 and 11 in cards and 10 in cards: 
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    total = sum(cards)
    return total

def compare(u_score, s_score):
    if u_score == s_score:
        return "It's a draw"
    elif u_score == 0:
        return "Congratulations!!! You win with a Blackjack"
    elif s_score == 0:
        return "You Lose, opponenet has a Blackjack"
    elif u_score > 21:
        return "You cross over!!!You Lose"
    elif s_score > 21:
        return "Opponent cross over!!!You Win"
    elif u_score > s_score:
        return "You Win!!!"
    else:
        return "You Lose!!!"
def blackjack_game():  
    print(logo)   
    user_cards = []
    system_cards = []
    # user_score = -1
    # system_score = -1

    for i in range(2):
        user_cards.append(dealer_cards())
        system_cards.append(dealer_cards())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        system_score = calculate_score(system_cards)
        print(f"Your cards: {user_cards}, user score: {user_score}")
        print(f"Computer's first card: {system_cards[0]}")
        if user_score == 0 or system_score == 0 or user_score > 21:
            is_game_over = True
        else:
            preference = input("Type 'yes' if you to draw another card and 'no' if you want to pass: ").lower()
            if preference == "yes":
                user_cards.append(dealer_cards())
                is_game_over = False
            else:
                is_game_over = True

    while system_score != 0 and system_score < 17:
        system_cards.append(dealer_cards())
        system_score = calculate_score(system_cards) 


    print(f"Your final cards: {user_cards}, final_user_score: {user_score}")
    print(f"System's final cards: {system_cards}, final_system_score: {system_score}")
    print(compare(user_score,system_score))


flag = True
while flag:
    choice = input("Do you want to play the game of Blackjack. Type 'yes' or 'no': ")
    if choice == "yes":
        print("\n"*30)
        blackjack_game()
        flag = True
    else:
        flag = False

    
 