from art import logo
print(logo)
print("Welcome to the secret auction program")
flag = True
bidders_data = {}

def highest_bid(bidding_dictionary):
    highest_value = 0
    for key in bidding_dictionary:
        bid_value = bidding_dictionary[key]
        if bid_value > highest_value:
            highest_value = bid_value
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_value}")

    
while flag:
    name = input("What is your name?: ")        #key
    price = int(input("What is your bid?: $"))  #value
    bidders_data[name] = price
    choice = input("Are there is any other bidders?Type 'yes' and 'no': ").lower()
    if choice == "yes":
        flag = True
        print("\n" * 100)   #clear the screen from the other bidders point of view by 100 spaces
    else:
        highest_bid(bidders_data)
        flag = False