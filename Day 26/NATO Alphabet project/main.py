import pandas
data_frame = pandas.read_csv("Day 26/NATO Alphabet project/nato_phonetic_alphabet.csv")   #Create the table format of nato_phonetic_alphabet.csv file
# print(data_frame)

"""Creating Dictionary using Dictionary comprehension and iterate over Pandas DataFrame"""
nato_phonetic_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}
# print(nato_phonetic_dict)


# #Without using the Exception Handling :
# user_word = input("Enter a word: ").upper()
# user_phonetic = [nato_phonetic_dict[letter] for letter in user_word]
# print(user_phonetic)


# #Using the Exception Handling : Using While Loop
# flag = True
# while flag:
#     user_word = input("Enter a word: ").upper()
#     try:
#         user_phonetic = [nato_phonetic_dict[letter] for letter in user_word]

#     except KeyError:
#         print("Sorry!!!Please enter the letter in the alphabet")
#         flag = True
#     else:
#         print(user_phonetic)
#         flag = False

#Using the Exception Handling : Using function
def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        user_phonetic = [nato_phonetic_dict[letter] for letter in user_word]

    except KeyError:
        print("Sorry!!!Please enter the letter in the alphabet")
        generate_phonetic()

    else:
        print(user_phonetic)

generate_phonetic()