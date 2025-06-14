import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Pypassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
# #Easy level
# password = ''
# for char in range(1, nr_letters + 1):
#     value1 = random.choice(letters)     #password += random.choice(letters)
#     password += value1
# for symbol in range(1, nr_symbols + 1):
#     value2 = random.choice(symbols)     #password += random.choice(symbols)
#     password += value2
# for number in range(1, nr_numbers + 1):
#     value3 = random.choice(numbers)     #password += random.choice(numbers)
#     password += value3
# print(f"Your password is {password}")

#Hard Level
password_list = []
for char in range(1, nr_letters + 1):
    value1 = random.choice(letters)     
    password_list.append(value1)
for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
     
random.shuffle(password_list)

print(password_list)

#1st method of concatenation
print("From 1st method")
password = ''
for char in password_list:
    password += char
print(f"Your password is {password}")

#Another process of concatenation
print("From 2nd method")
password = ''
for char in range(0, nr_letters + nr_symbols + nr_numbers):
    password = password + password_list[char]
print(f"Your password is {password}")

