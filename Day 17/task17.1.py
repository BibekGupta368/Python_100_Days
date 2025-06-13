# #Topic 1
# class User:
#     pass

# user_1 = User()
# user_1.id = "001"
# user_1.username = "Bibek"
# print(user_1.username)
# user_2 = User()
# user_2.id = "002"
# user_2.name = "Abhinav"
# print(user_2.name)

# #Topic 2
# class User:
#     #Declaring a constructor with attributes 'user_id' and 'username'
#     def __init__(self,user_id,username):
#         self.user_id = user_id
#         self.username = username
#         self.followers = 0
# user_1 = User("001", "Bibek")
# print(user_1.username) 
# print(user_1.followers)
# user_2 = User("002", "Abhinav")
# print(user_2.username)
# print(user_2.followers)

# #Topic 3
# class User:
#     #Declaring a constructor with attributes 'user_id' and 'username'
#     def __init__(self,user_id,username):
#         self.user_id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#     #Declaring a method to class
#     def follow(self,user):
#         user.followers += 1
#         self.following += 1

# user_1 = User("001", "Bibek")
# print(user_1.username) 
# print("Initially")
# print(user_1.followers)
# print(user_1.following)

# user_2 = User("002", "Abhinav")
# print(user_2.username)
# print("Initially")
# print(user_2.followers)
# print(user_1.following)

# print("Now")
# user_1.follow(user_2)  #calling the method to class

# print("User_1")
# print(user_1.followers)
# print(user_1.following)

# print("User_2")
# print(user_2.followers)
# print(user_2.following)




import random
question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

print(random.choice(question_data))