alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from caesar_cipher_art import logo
print(logo)
# # Topic : 1st method 
# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ''
#     for letter in original_text:
#         if letter not in alphabet:
#             output_text += letter
#         else:      
#             #current index of letter
#             current_index = alphabet.index(letter)
#             if encode_or_decode == "encode":
#                 #Encoded index of letter after adding the shift amount
#                 new_index = current_index + shift_amount
#                 new_index = new_index % len(alphabet) # always gives the value 0-25
#                 #Encoded letter for the given letter
#                 encoded_letter = alphabet[new_index]
#                 #Adding to the empty string
#                 output_text += encoded_letter
#             else:
#                 #Decoded index of letter after subtracting the shift amount
#                 new_index = current_index - shift_amount
#                 new_index %= len(alphabet)  # always gives the value 0-25
#                 #Decoded letter for the given letter
#                 decoded_letter = alphabet[new_index]
#                 #Adding to the empty string
#                 output_text += decoded_letter
#     print(f"Here's the {encode_or_decode}ed result: {output_text} ")

# Topic : 2nd method more shorter
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            #current index of letter
            current_index = alphabet.index(letter)
            if encode_or_decode == "decode": 
                shift_amount *= -1                     #shift_amount *= -1(It is a bug which we cleared by adding the line 50 )
            #index of letter after adding the shift amount
            new_index = current_index + shift_amount
            new_index = new_index % len(alphabet) # always gives the value 0-25
            #final letter for the given letter
            final_letter = alphabet[new_index]
            #Adding to the empty string
            output_text += final_letter
            #Turning back the shift_amount value to the original value
            shift_amount = shift
    print(f"Here's the {encode_or_decode} d result: {output_text} ")
   

flag = False
while not flag:
    desire = input("Type 'encode to encrypt the message and type 'decode to decrypt the message:\n").lower()
    text = input("Enter your message:\n").lower()
    shift = int(input("Enter the shift number you want:\n"))

    caesar(original_text = text, shift_amount = shift,encode_or_decode = desire)
    choice = input("Type 'yes' if you want to go again.Otherwise just type 'no':\n" ).lower()
    if choice == "yes":
        flag = False
    else:
        flag = True  
        print("Goodbye!!!")