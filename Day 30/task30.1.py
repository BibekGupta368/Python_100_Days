# #Topic 1
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")




# #Topic 2 : raise exception
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is the error i made up.")
   


# #Topic 3 : raise exception
# Height = float(input("Height: "))
# Weight = int(input("Weight: "))

# if Height > 3:
#     raise ValueError("Human heights should be less than 3 meters")

# bmi = Weight / Height ** 2
# print(bmi)



# #Topic 4 : IndexErrorHandling Coding Exercise
# """
# fruits = ["Apple", "Pear", "Orange"]

# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")

# make_pie(4)

# Comments:
# IndexError Handling
# Issue 
# We've got some buggy code. Try running the code. The code will crash and give you an IndexError.

# This is because we're looking through the list of fruits for an index that is out of range. 

# Objective 
# Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie". 
# IMPORTANT: The exception handling should NOT allow each fruit to be printed when there is an exception. e.g. it should not print out Apple pie, Pear pie and Orange pie, when there is an exception it should only print "Fruit pie". 
# """

# fruits = ["Apple", "Pear", "Orange"]
 
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#   try:
#     fruit = fruits[index]
#   except IndexError:
#     print("Fruit pie")
#   else:
#     print(fruit + " pie")
 
# make_pie(4)




# #Topic 5 : KeyErrorHandling Coding Exercise
# """
# KeyError Handling
# We've got some buggy code, try running the code. The code will crash and give you a KeyError.
# This is because some of the posts in the facebook_posts don't have any "Likes". 
# Objective 
# Use what you've learnt about exception handling to prevent the program from crashing. 

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]

# def count_likes(posts):

#     total_likes = 0
#     for post in posts:
#         total_likes = total_likes + post['Likes']
    
#     return total_likes


# count_likes(facebook_posts)

# """

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
 
 
# def count_likes(posts):
 
#     total_likes = 0
#     for post in posts:
#       try:
#         total_likes = total_likes + post['Likes']
#       except KeyError:
#         pass 
    
#     return total_likes
 
 
# print(count_likes(facebook_posts))
