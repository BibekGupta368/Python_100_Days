# #List comprehension : Topic 1 : Getting the new_list by adding the 1 to the numbers
# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)




# #List comprehension : Topic 2
# name = "Bibek"
# new_list = [letter for letter in name]
# print(new_list)




# #List comprehension : Topic 3 : Getting the numbers in the range(1, 5) with the double values
# numbers = range(1,5)
# new_list = [2*num for num in numbers]
# print(new_list)




# #Conditional List comprehension : Topic 4 : Getting the list of names whose length is less than 5
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
# print(short_names)




# #Conditional List comprehension : Topic 5 : Getting the list of names whose length is greater than 4 and in uppercase form
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)




# #List comprehension : Topic 6 : You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared. 
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n*n for n in numbers]
# print(squared_numbers)




# #List comprehension : Topic 7 :First, use list comprehension to convert the list_of_strings to a list of integers called numbers.   
# """
# Then use list comprehension again to create a new list called result.
# This new list should only contain the even numbers from the list numbers. 
# """
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(item) for item in list_of_strings]
# result = [n for n in numbers if n%2 == 0]
# print(result)




# #List comprehension : Topic 8 
# """
# Data Overlap
# 💪 This exercise is HARD 💪 
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
# You are going to create a list called result which contains the numbers that are common in both files. 
# e.g. if file1.txt contained: 
# 1 
# 2 
# 3
# and file2.txt contained: 
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop.
# """
# with open("Day 26\\file1.txt") as file1:
#     list1 = file1.readlines()

# with open("Day 26\\file2.txt") as file2:
#     list2 = file2.readlines()

# result = [int(num) for num in list1 if num in list2] 
# print(result)





# # Dictionary comprehension : Topic 9
# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
# """Dictionary Creation"""
# student_scores = {student:random.randint(1,100) for student in names}
# print(f"student_scores = {student_scores}")





# # Conditional Dictionary comprehension : Topic 10
# import random
# names = ['Bibek', 'Roy', 'Tanu', 'Abhinav', 'Sujit', 'Stiti']

# """Dictionary Creation"""
# student_scores = {student:random.randint(1,100) for student in names}
# print(f"student_scores = {student_scores}")

# """Conditional Dictionary Creation"""
# passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
# print(f"passed_students = {passed_students}")






# #Dictionary comprehension 1 : Topic 11
# """
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.   
# Try Googling to find out how to convert a sentence into a list of words.  *
# *Do NOT** Create a dictionary directly.
# Try to use Dictionary Comprehension instead of a Loop. 
# To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.
# """
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# #converting the given sentence into a list of words
# sentence_list_format = sentence.split()
# print(sentence_list_format)
# """"Creating Dictionary"""
# result = {word:len(word) for word in sentence_list_format}
# print(f"result = {result}")





# #Dictionary comprehension 2 : Topic 12
# """
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 
# To convert temp_c into temp_f use this formula: 
# (temp_c * 9/5) + 32 = temp_f
# """
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:((temp_c * 9/5) + 32) for (day,temp_c) in weather_c.items()}
# print(f"weather_f = {weather_f}")




