import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = []
for letter in chosen_word:
    placeholder.append("_")

guess = input("Guess a Letter: ").lower()

# Create a "display" that puts the guess letter in the right spot
index = 0
for letter in chosen_word:
    if guess == letter:
        placeholder[index] = guess
    
    index += 1