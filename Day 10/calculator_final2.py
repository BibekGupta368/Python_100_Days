from calculator_art import logo
print(logo)

def calculate(n1,n2,operation):
    if operation == "+":
        return n1 + n2
    elif operation == "-": 
        return n1-n2
    elif operation == "*":
        return n1 * n2
    else:
        return n1/n2

def calculator():
    num1 = float(input("What is the first number: "))
    print("+")
    print("-")
    print("*")
    print("/")
    flag = True 
    while flag:
        operation =input("Pick an operation: ")

        num2 = float(input("What is the next number: "))

        result = calculate(num1,num2,operation)
        print(f"{num1} {operation} {num2} = {result}")
        
        choice = input(f"Type 'continue' if you want to continue calculating with current answer {result} and 'new' if you want to start the new calculation and 'quit' if you want to off the calculator: ").lower()
        if choice == "continue":
            num1 = result 
            flag =True
        elif choice == "new":
            print("\n"*30)
            flag = False
            calculator()
        else:                     #choice == "quit":
            flag = False

calculator()