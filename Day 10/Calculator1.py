from calculator_art import logo
print(logo)

def addition(n1,n2):
    return n1 + n2
def substraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1 * n2
def division(n1,n2):
    return n1/n2

def calculator():
    num1 = float(input("What is the first number: "))
    lists = ["Addition", "Substraction", "Multiplication", "Division"]
    for list in lists:
        if list == "Addition":
            print("+")
        elif list == "Substraction":
            print("-")
        elif list == "Multiplication":
            print("*")
        else:
            print("/")
    # # OR
    # print("+")
    # print("-")
    # print("*")
    # print("/")
    flag = True
    while flag:
        operation =input("Pick an operation: ")
        num2 = float(input("What is the next number: "))

        if operation == "+":
            add = addition(num1, num2)
            print(f"Result:{add}")
            choice = input(f"Type 'continue' if you want to continue calculating with current answer {add} and 'new' if you want to start the new calculation and 'quit' if you want to off the calculator: ").lower()
            if choice == "continue":
                num1 = add 
                flag =True
            elif choice == "new":
                print("\n"*30)
                flag = False
                calculator()
            else:                     #choice == "quit":
                flag = False
        elif operation == "-":
            substract = substraction(num1, num2)
            print(f"Result:{substract}")
            choice = input(f"Type 'continue' if you want to continue calculating with current answer {substract} and 'new' if you want to start the new calculation and 'quit' if you want to off the calculator: ").lower()
            if choice == "continue":
                num1 = substract
                flag =True
            elif choice == "new":
                print("\n"*30)
                flag = False
                calculator()
            else:                     #choice == "quit":
                flag = False
        elif operation == "*":
            multiply = multiplication(num1, num2)
            print(f"Result:{multiply}")
            choice = input(f"Type 'continue' if you want to continue calculating with current answer {multiply} and 'new' if you want to start the new calculation and 'quit' if you want to off the calculator: ").lower()
            if choice == "continue":
                num1 = multiply 
                flag =True
            elif choice == "new":
                print("\n"*30)
                flag = False
                calculator()
            else:                     #choice == "quit":
                flag = False
        else:
            divide = division(num1, num2)
            print(f"Result:{divide}")
            choice = input(f"Type 'continue' if you want to continue calculating with current answer {divide} and 'new' if you want to start the new calculation and 'quit' if you want to off the calculator: ").lower()
            if choice == "continue":
                num1 = division 
                flag =True
            elif choice == "new":
                print("\n"*30)
                flag = False
                calculator()
            else:                     #choice == "quit":
                flag = False

calculator()