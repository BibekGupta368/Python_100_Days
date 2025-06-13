menu_card = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    #Returns True if resources are sufficient and false if there is not enough resources
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Extremely sorry sir there is not enough {item}.")
            return False
    return True

def process_coins():
    #Process the coins 
    print("Please insert coin.")
    coin1 = int(input("How many quarter: "))
    coin2 = int(input("How many dimes: "))
    coin3 = int(input("How many nickles: "))
    coin4 = int(input("How many pennies: "))
    total = coin1 * 0.01 + coin2 * 0.10 + coin3 * 0.05 + coin4 *0.25
    return total
def is_transaction_successful(money_received, drink_cost):
    #Return True when the payment is sufficient enough, or False if payment is insufficient
    if money_received >= drink_cost:
        change = round((money_received - drink_cost), 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("You don't have the enough money.Money refunded")
        return False
def processing_coffee(drink_name, order_ingredients):
    #Updating the available  ingredients from the resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")  
profit = 0
flag = True
while flag:
    choice = input("What would you like? (espresso/latte/cappuccino/off): ")
    if choice == "off":
        print("Machine Turned off")
        flag = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu_card[choice]
        coffee_ingredients = drink["ingredients"]
        result1 = is_resource_sufficient(coffee_ingredients)
        if result1 == True:
            payment = process_coins()
            result2 = is_transaction_successful(payment, drink["cost"])
            if result2 == True:
                 processing_coffee(choice, coffee_ingredients)



        