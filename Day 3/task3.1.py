# #Even and odd checker
# number = int(input("Enter the number you have to check "))
# if number % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# #Nested if and else
# print("Welcome to the roller coaster")
# height = int(input("What is your height? "))
# if height >= 120:
#     print("you can ride")
#     age = int(input("What is your age? "))
#     if age <= 18:
#         print("Pay 7$")
#     else:
#         print("Pay 12$")    
# else:
#     print("you cant ride")


# #Nested if,elif and else
# print("Welcome to the roller coaster")
# height = int(input("What is your height? "))
# if height >= 120:
#     print("you can ride")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Pay 5$")  
#     elif age >= 12 and age <= 18:  ## also you can use elif 12 <= age <= 18:
#         print("Pay 7$")    
#     else:
#         print("pay 12$")
# else:
#     print("you cant ride")    


# #other concept without using and
# print("Welcome to the roller coaster")
# height = int(input("What is your height? "))
# if height >= 120:
#     print("you can ride")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Pay 5$") 
#     elif age >18:
#         print("12$")
#     else:
#         print("7$")   
# else:
#     print("you cant ride")    



# #Bmi calculator
# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# # 🚨 Do not modify the values above
# # Write your code below 👇
# if bmi < 18.5:
#    print("Under weight.")
# elif 18.5 <= bmi < 25:
#    print("Normal weight.")
# elif 25 <= bmi <30 :
#    print("Over weight.")
# else:
#     print("Not a valid bmi.")
   

# # Multiple if statements
# print("Welcome to the roller coaster")
# height = int(input("What is your height? "))
# if height >= 120:
#   print("you can ride")
#   age = int(input("What is your age? "))
#   if age < 12:
#      bill = 5
#      print("Child ticket price is 5$")  
#   elif age >= 12 and age <= 18:
#      bill = 7
#      print("Youth ticket price is 7$")    
#   else:
#     bill = 12
#     print("Adult ticket price is 12$")
#   #Extra condition for photos
#   wants_photos = input("Do you want to have your photo? Yes or No ") 
#   if wants_photos == "yes":
#      #add 3$ to the ticket
#      bill += 3
#   print(f"The final ticket price is {bill}$")  
# else:
#     print("you cant ride")    



# #Logical operator ticket pricing
# print("Welcome to the roller coaster")
# height = int(input("What is your height? "))
# bill=0
# if height >= 120:
#   print("you can ride")
#   age = int(input("What is your age? "))
#   if age < 12:
#      bill = 5
#      print("Child ticket price is 5$")  
#   elif age >= 12 and age <= 18:
#      bill = 7
#      print("Youth ticket price is 7$")    
#   elif age >= 44 and age <= 55:
#       #bill = 0 if you put this here then you dont have to initialize bill = 0 in top
#       print("Ride is free for the given age")  
#   else:
#     bill = 12
#     print("Adult ticket price is 12$")
#   #Extra condition for photos
#   wants_photos = input("Do you want to have your photo? Yes or No ") 
#   if wants_photos == "yes":
#      #add 3$ to the ticket
#      bill += 3
#   print(f"The final ticket price is {bill}$")  
# else:
#     print("you cant ride")    
   