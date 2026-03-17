# TODO-1: Import and print the logo from art.py when the program starts
import art

print(art.caesar_logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
        
    for letter in original_text:
        # TODO-2: What happens if the user enters a number/symbol/space?
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    
    print(f"Here is your {encode_or_decode}d result: {output_text}")

# TODO-3: Can you figure out a way to restart the cipher program?
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye")