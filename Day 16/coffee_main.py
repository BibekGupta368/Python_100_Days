from menu_card import Menu
from coffee_processing import CoffeeProcessing
from money_processing import MoneyProcessing

menu_card = Menu()
coffee_processing = CoffeeProcessing()
money_processing = MoneyProcessing()

flag = True
while flag:
    options = menu_card.get_items()
    choice = input(f"What would you like? {options}off: ")
    if choice == "off":
        print("The machine is turning off")
        flag = False
    elif choice == "report":
        coffee_processing.report()
        money_processing.report()
    else:
        drink = menu_card.find_drink(choice)
        result = coffee_processing.is_resource_sufficient(drink)
        if result == True:
            if money_processing.make_payment(drink.cost):
                coffee_processing.make_coffee(drink) 
        






