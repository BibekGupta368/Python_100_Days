'''Topic 1: In the below code, we want to print the all the elements
 in b_list same as in a_list but instead of printing that it is printing
 single element.It's a bug and we have to fix it'''
# import random
# import maths

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         # print(new_item)
#         new_item = maths.add(new_item, item)
#     b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])

'''Topic 2: In  order to fix the bug in the above topic 1 code, we simply 
move the the line "b_list.append(new_item)" inside the "for" Loop
'''
import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        # print(new_item)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])




# #Topic 3
# def odd_or_even(number):
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."
# print(odd_or_even(15))




# #Topic 4:Wrong
# # Target is the number up to which we count
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 or number % 5 == 0:
#             print("FizzBuzz")
#         if number % 3 == 0:
#             print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         else:
#             print([number])




# #Topic 4 :Correct version
# # Target is the number up to which we count
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)
# fizz_buzz(6)