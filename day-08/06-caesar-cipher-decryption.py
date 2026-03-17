alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet) # range 0 - 25
        encrypted_text += alphabet[shifted_position]
    
    print(f"Encrypted Text: {encrypted_text}")

encrypt(original_text=text, shift_amount=shift)

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' forwards in the alphabet backwards
#  by the 'shift_amount' and print the decrypted text.

def decrypt(original_text, shift_amount):
    decrypted_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        decrypted_text += alphabet[shifted_position]

    print(f"Decrypted Text: {decrypted_text}")

decrypt(original_text=text, shift_amount=shift)