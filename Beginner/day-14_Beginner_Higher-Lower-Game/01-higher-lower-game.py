import random
import art
import persons
import os

repeat_game = True

def print_logo():
    os.system("clear")
    print(art.higher_lower_logo)

while repeat_game:
    streak = 0
    guessed_right = True
    guess = ""

    person1 = random.choice(list(persons.PERSONS))

    while guessed_right:
        person2 = random.choice(list(persons.PERSONS))

        print_logo()

        print(f"Compare A: {person1}")
        print(art.vs_logo)
        print(f"Compare B: {person2}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if guess == "a" and persons.PERSONS[person1] > persons.PERSONS[person2]:
            streak += 1
        elif guess == "b" and persons.PERSONS[person2] > persons.PERSONS[person1]:
            streak += 1
            person1 = person2
        else:
            guessed_right = False
            break

    if guessed_right == False:
        print_logo()
        print(f"Sorry, that's wrong. Final score: {streak}")
        repeat_game_input = input("Do you want to play again? Type 'yes' or 'no': ")

        if repeat_game_input == "no":
            repeat_game = False

