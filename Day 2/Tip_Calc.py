print("Welcome to the tip Calculator")
total_bill = float(input("What was your total bill? $"))
tip = int(input("How much percentage tip would you like to give? 10, 12, or 15? ")) #can be use as float as well
total_bill_after_tip = float(total_bill) + (tip / 100 * total_bill)
No_of_people = int(input("How many people to split the bill? ")) #can be use as float as well
each = total_bill_after_tip / No_of_people
# each = (total_bill + (tip / 100 * total_bill)) / No_of_people #can be used directly instead of line4 and line6
final_amount = round(each, 2)
print(f"Each person should pay: ${final_amount}")
# print("Each person should pay: $" + str(final_amount))
# print(type(total_bill))
# print(type(tip))
# print(type(No_of_people))