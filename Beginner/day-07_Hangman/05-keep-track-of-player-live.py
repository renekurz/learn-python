import random

# Get Hangman Pics - https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = []
for letter in chosen_word:
    placeholder.append("_")

# implement lives
lives = 6
hangman_index = 0

while "_" in placeholder:
    display = ""
    right_letter = False
    guess = input("Guess a Letter: ").lower()

    index = 0
    for letter in chosen_word:
        if guess == letter:
            placeholder[index] = guess
            right_letter = True
        
        index += 1

    if right_letter == False:
        lives -= 1
        hangman_index += 1

    for letter in placeholder:
        display += letter

    print(HANGMANPICS[hangman_index])
    print(display)
    print(f"Lives: {lives}")

    if lives == 0:
        print("You lose!")
        print(f"The word was: {chosen_word}")
        break
