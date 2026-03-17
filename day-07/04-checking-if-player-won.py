import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = []
for letter in chosen_word:
    placeholder.append("_")

# Use a while loop to let the user guess again
# Display the placeholder
while "_" in placeholder:
    display = ""
    guess = input("Guess a Letter: ").lower()

    index = 0
    for letter in chosen_word:
        if guess == letter:
            placeholder[index] = guess
        
        index += 1

    for letter in placeholder:
        display += letter

    print(display)