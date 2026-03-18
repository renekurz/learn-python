import random
import art

print(art.number_guessing_logo)

print("Welcome to the Number Guessing Game!")

NUMBER_TO_GUESS = random.randint(1, 100)
EASY = 10
HARD = 5

print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number_of_guesses = 0

if difficulty == "easy":
    number_of_guesses = EASY
else:
    number_of_guesses = HARD

while number_of_guesses > 0:
    print(f"You have {number_of_guesses} attempts remaining to guess the number")

    guess = int(input("Make a guess: "))

    if NUMBER_TO_GUESS > guess:
        print("Too low")
    elif NUMBER_TO_GUESS < guess:
        print("Too high")
    elif NUMBER_TO_GUESS == guess:
         print(f"You got it! The answer was {NUMBER_TO_GUESS}")
         break
    
    number_of_guesses -= 1
    
if number_of_guesses == 0:
    print(f"The searched number was: {NUMBER_TO_GUESS}")
    print("You've run out of guesses. Restart the program to run again.")