print("Welcome to the pizza Delivery program!")
size = input("Which size of pizza do you want? S,M or L : ")
pepproni = input("Do you want to add pepproni on your pizza? Yes or No : ")
extra_cheese =input("Do you want to add extra cheese on your pizza? Yes or No : ")
bill = 0
if size == "S":
  bill += 15
  print("Small sized pizza price is 15$")
  if pepproni == "Yes":
     bill += 2
     print("Pepproni price is 2$")
elif size == "M":
  bill += 20
  print("Medium sized pizza price is 20$")
  if pepproni == "Yes":
     bill += 3
     print("Pepproni price is 3$")  
elif size == "L":
  bill += 25
  print("Large sized pizza price is 25$")
  if pepproni == "Yes":
     bill += 3
     print("Pepproni price is 3$")     
else:
   print("Invalid input!")
#Extra condition for cheese
if extra_cheese == "Yes":
   #add 1$ to the bill
   bill += 1
   print("Extra Cheese price is 1$")  
   
print(f"The final bill amount to be paid {bill}$")
 