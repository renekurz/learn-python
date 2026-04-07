alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the 'encrypt()' and 'decrypt()' functions into a single function called 'caesar()'.
#  Use the value of the user chosen direction variable to determine which functionality to use.
#  call the caesar function instead of encrypt/decrypt and pass in all three variables: direction / text / shift.

def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
        
    for letter in original_text:

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    
    print(f"Here is your {encode_or_decode}d result: {output_text}")

caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)