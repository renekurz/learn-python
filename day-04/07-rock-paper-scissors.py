# Rock Paper Scissors Game:
# This program simulates the classic Rock–Paper–Scissors game between the user
# and the computer. The user selects a number representing their choice, while
# the computer randomly picks one. The program then compares both choices and
# displays whether the user wins, loses, or if the game ends in a draw.

import random

rock = '''
    _______
---'   ____)
    (_____)
    (_____)
    (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock, paper, scissors]
computer_random_int = random.randint(0,2)
computer_choice = rock_paper_scissors[computer_random_int]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("Your choice:\n" + rock_paper_scissors[your_choice])
print("Computer choice:\n" + rock_paper_scissors[computer_random_int])

# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

if your_choice >= 3 or your_choice < 0:
    print("You typed an invalid number. You lose!")
elif your_choice == 0 and computer_random_int == 2:
    print("You win!")
elif computer_random_int == 0 and your_choice == 2:
    print("You lose!")
elif computer_random_int > your_choice:
    print("You lose!")
elif your_choice > computer_random_int:
    print("You win!")
elif computer_random_int == your_choice:
    print("It's a draw!")