alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from caesar_cipher_art import logo
print(logo)
def encrypt(text, shift):    #def encrypt(original_text, shift_amount):
    encoded_text = ''
    for letter in text:
        if letter not in alphabet:
            encoded_text += letter
        else: 
        #current index of letter
            current_index = alphabet.index(letter)
            #Encoded index of letter after adding the shift amount
            new_index = current_index + shift
            new_index = new_index % len(alphabet) # always gives the value 0-25
            #Encoded letter for the given letter
            encoded_letter = alphabet[new_index]
            #Adding to the empty string
            encoded_text += encoded_letter
    print(f"Here's the encoded result: {encoded_text} ")

def decrypt(text, shift):     #def decrypt(original_text, shift_amount):
    decoded_text = ''
    for letter in text:
        if letter not in alphabet:
            decoded_text += letter
        else: 
            #current index of letter
            current_index = alphabet.index(letter)
            #Decoded index of letter after subtracting the shift amount
            new_index = current_index - shift
            new_index %= len(alphabet)  # always gives the value 0-25
            #Decoded letter for the given letter
            decoded_letter = alphabet[new_index]
            #Adding to the empty string
            decoded_text += decoded_letter
    print(f"Here's the decoded result: {decoded_text} ")

flag = True
while flag:
    desire = input("Type 'encode to encrypt the message and type 'decode to decrypt the message:\n").lower()
    text = input("Enter your message:\n").lower()
    shift = int(input("Enter the shift number you want:\n"))

    if desire == "encode":
        encrypt(text,shift)      #encrypt(original_text = text, shift_amount = shift)
        choice = input("Type 'yes' if you want to go again.Otherwise just type 'no':\n" ).lower()
        if choice == "yes":
            flag = True
        else:
            flag = False
            print("Goodbye!!!")
         
    else:
        decrypt(text,shift)      #decrypt(original_text = text, shift_amount = shift)
        choice = input("Type 'yes' if you want to go again.Otherwise just type 'no':\n" ).lower()
        if choice == "yes":
            flag = True
        else:
            flag = False
            print("Goodbye!!!")