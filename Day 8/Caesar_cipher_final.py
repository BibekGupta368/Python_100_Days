alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import caesar_cipher_art 
print(caesar_cipher_art .logo)
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
    if encode_or_decode == "decode":
        shift_amount *= -1      #shift_amount *= -1(It is a bug which we cleared by taking it out of the 'else' part of the 'for' loop)
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:  
            #current index of letter
            current_index = alphabet.index(letter)   
            #index of letter after adding the shift amount
            new_index = current_index + shift_amount
            new_index = new_index % len(alphabet) # always gives the value 0-25
            #final letter for the given letter
            final_letter = alphabet[new_index]
            #Adding to the empty string
            output_text += final_letter          
    print(f"Here's the {encode_or_decode}d result: {output_text} ")
   

flag = True
while flag:
    desire = input("Type 'encode to encrypt the message and type 'decode to decrypt the message:\n").lower()
    text = input("Enter your message:\n").lower()
    shift = int(input("Enter the shift number you want:\n"))

    caesar(original_text = text, shift_amount = shift,encode_or_decode = desire)
    choice = input("Type 'yes' if you want to go again.Otherwise just type 'no':\n" ).lower()
    if choice == "yes":
        flag = True
    else:
        flag = False 
        print("Goodbye!!!")