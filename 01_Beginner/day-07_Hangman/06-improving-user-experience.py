import random
import hangman_words
import hangman_art

# TODO-1: Update the word list to use the 'word_list' from hangman_words.py
# TODO-2: Update the code to use the stages from the file hangman_art.py
# TODO-3: Import the logo from hangman_art.py and print it at the start of the game
# TODO-4:
#   - If the user has entered a letter they've already guessed, print the letter and let them know.
#   - We should not deduct a life for this.
#   - e.g. You've already guessed a
# TODO-5:
#   - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#   - e.g. You guessed d, that's not in the word. You lose a life.
# TODO-6: If the player didn't lose a life yet, there should be no hangman art


chosen_word = random.choice(hangman_words.word_list)

placeholder = []
for letter in chosen_word:
    placeholder.append("_")

lives = 7
hangman_index = -1
guessed_letters = []

print(hangman_art.hangman_logo)

while "_" in placeholder:
    display = ""
    right_letter = False

    guess = input("Guess a Letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    else:
        guessed_letters.append(guess)

        index = 0
        for letter in chosen_word:
            if guess == letter:
                placeholder[index] = guess
                right_letter = True
            
            index += 1

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if right_letter == False:
            lives -= 1
            hangman_index += 1

        for letter in placeholder:
            display += letter

        if hangman_index >= 0:
            print(hangman_art.HANGMANPICS[hangman_index])
        
        print(display)
        print(f"Lives: {lives}")

        if lives == 0:
            print("You lose!")
            print(f"The word was: {chosen_word}")
            break
