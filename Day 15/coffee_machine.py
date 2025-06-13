#Initial resources that machine have initially
water = 300
milk = 200
coffee = 100
money = 0

def processing(input1):
    coin1 = int(input("How many quarter: "))
    coin2 = int(input("How many dimes: "))
    coin3 = int(input("How many nickles: "))
    coin4 = int(input("How many pennies: "))
    total_sum = coin1 * 0.01 + coin2 * 0.10 + coin3 * 0.05 + coin4 *0.25
    return total_sum


flag = True
while flag:
    input1 = input("What would you like?(Espresso/Latte/Cappuccino/off):  ").lower()
    if input1 == "espresso":
        if milk >= 50 and coffee >= 18:
            print("Please insert coin.")
            result = processing(input1)
            if result >= 1.5:
                change = result - 1.50
                #Updating the resources after purchasing the coffee
                water -= 50
                coffee -= 18
                money += 1.50
                flag = True
                print(f"Here's ${round((change),2)} in change")
                print("Enjoy your expresso sir☕.")
            else:
                print("You don't have the enough money.Money refunded")
        else: 
            print("You don't have enough resources")
            if water < 50 and coffee < 18:
                print("Don't have enough water and coffee")
            elif water < 50:
                print("Don't have enough water")
            else:
                print("Don't have enough coffee")

    elif input1 == "latte":
        if milk >= 200 and coffee >= 24:
            print("Please insert coin.")
            result = processing(input1)
            if result >= 2.50:
                change = result - 2.50
                #Updating the resources after purchasing the coffee
                water -= 200
                coffee -= 24
                milk -=150
                money += 2.50
                flag = True
                print(f"Here's ${round((change),2)} in change")
                print("Enjoy your Latte sir☕.")
            else:
                print("You don't have the enough money.Money refunded")
        else: 
            print("You don't have enough resources")
            if water < 200 and coffee < 24:
                print("Don't have enough water and coffee")
            elif water < 200 and milk < 150:
                print("Don't have enough water and milk")
            elif coffee < 24 and milk < 150:
                print("Don't have enough coffee and milk")
            elif water < 200:
                print("Don't have enough water")
            elif coffee < 24:
                print("Don't have enough coffee")
            else:
                print("Don't have enough milk")
                    
       
    elif input1 == "cappuccino":
        if water >= 250 and coffee >= 24 and milk >= 100: 
            print("Please insert coin.")
            result = processing(input1)
            if result >= 3:
                change = result - 3.00
                #Updating the resources after purchasing the coffee
                water -= 250
                coffee -= 24
                milk -= 100
                money += 3.00
                flag = True
                print(f"Here's ${round((change),2)} in change")
                print("Enjoy your Cappucino sir☕.")
                        
            else:
                print("You don't have the enough money.Money refunded")
        else: 
            print("You don't have enough resources")
            if water < 250 and coffee < 24:
                print("Don't have enough water and coffee")
            elif water < 250 and milk < 100:
                print("Don't have enough water and milk")
            elif coffee < 24 and milk < 100:
                print("Don't have enough coffee and milk")
            if water < 250:
                print("Don't have enough water")
            if coffee < 24:
                print("Don't have enough coffee")
            else:
                print("Don't have enough milk")
                
    elif input1 == "report":
        print(f"water = {water}ml")
        print(f"milk = {milk}ml")
        print(f"cofffee = {coffee}gm")
        print(f"money = ${money}")
        flag = True
    elif input1 == "off":
        flag = False
        print("Machine turned off")
    else: 
        print("Invalid Entry!!!")
        flag = True
 