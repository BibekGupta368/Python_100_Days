import random
from hl_data import data_list
from hl_art import logo1,logo2

def higher_lower():
    #printing the logo
    print(logo1)
    data2 = random.choice(data_list) 
    flag = True
    score = 0
    while flag:
        #Making the data at position B become the next data at position A                                             
        data1 = data2                # data1 is now behave as a dictionary

        #Choosing the second random data as 'B' from the given data_list 
        data2 = random.choice(data_list)  # data2 is now behave as a dictionary

        if data1 == data2:
            data2 = random.choice(data_list)

        print("Compare A: " + data1['name'] + ", " + data1['description'] + ", " + "from " + data1['country'])

        print(logo2)

        print("Against B: " + data2['name'] + ", " + data2['description'] + ", " + "from " + data2['country'])

        choice = input("Who has more followers? Type 'A' or 'B': ")
        print("\n" *20)
        print(logo1)
        if choice == "A":
            if data1['follower_count'] > data2['follower_count']:
                score += 1
                print(f"You're absolutely right!!!, current score = {score}")
                flag = True
            elif data2['follower_count'] > data1['follower_count']:
                print(f"Opps that's wrong!!!,final score = {score}")
                flag = False
            else:
                print(f"Both have the same follower count")
                flag = True

        else: #choice == "B":
            if data2['follower_count'] > data1['follower_count']:
                score += 1
                print(f"You're absolutely right!!!, current score = {score}")
                flag = True
            elif data1['follower_count'] > data2['follower_count']:
                print(f"Opps that's wrong!!!,final score = {score}")
                flag = False
            else:
                print(f"Both have the same follower count")
                flag = True

flag1 = True
while flag1:
    choice1 = input("Do you want to play the HIGHER LOWER GAME? Type 'yes' or 'no': ")
    if choice1 == "yes":
        higher_lower()
        flag1 = True
    else:
        flag1 = False