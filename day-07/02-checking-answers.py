import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a Letter: ").lower()
print(f"Guess: {guess}")

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")