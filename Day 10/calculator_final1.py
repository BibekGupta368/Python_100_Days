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

# Here i have pushed the key and values into the dictionary,you can also create manually
calculator_dictionary = {}
values = [addition, substraction, multiplication, division]
keys = ["+", "-", "*", "/"]
#Creating the dictionary by adding keys as "+","-","*","/" values as "Addition", "Substraction", "Multiplication", "Division"
for i in range(0,4):
    calculator_dictionary[keys[i]] = values[i] 
# print(calculator_dictionary) 

# # Manually creation of dictionary(It is valid only when there is the function defined of all the values and keys are used inside that function)
# calculator_dictionary = {
#     "+": addition,
#     "-": substraction,
#     "*": multiplication, 
#     "/": division    
# }
   
def calculator():
    num1 = float(input("What is the first number: "))
    flag = True
    while flag:
        #Printing the symbols using dictionary
        for operation in calculator_dictionary:
            print(operation)

        operation = input("Pick an operation: ")

        num2 = float(input("What is the next number: "))

        result = calculator_dictionary[operation](num1, num2)
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

