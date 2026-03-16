# PyPassword Generator:
# This program generates a random password based on user preferences.
# The user specifies how many letters, numbers, and symbols the password
# should contain. It creates an "easy" version where characters are added
# in order, and a "hard" version where all characters are shuffled to
# produce a more secure and random password.

import random

print("Welcome to the PyPassword Generator!")

count_letters = int(input("How many letters would you like in your password?\n"))
count_numbers = int(input("How many numbers would you like?\n"))
count_symbols = int(input("How many symbols would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Easy version - concat all
easy_password = ""
for letter in range(1, count_letters + 1):
    easy_password += random.choice(letters)

for number in range(1, count_numbers + 1):
    easy_password += random.choice(numbers)

for symbol in range(1, count_symbols + 1):
    easy_password += random.choice(symbols)

print(f"Easy version password: {easy_password}")


# Hard version - random
hard_password = ""
hard_password_list = []

for letter in range(1, count_letters + 1):
    hard_password_list.append(random.choice(letters))

for number in range(1, count_numbers + 1):
    hard_password_list.append(random.choice(numbers))

for symbol in range(1, count_symbols + 1):
    hard_password_list.append(random.choice(symbols))

random.shuffle(hard_password_list)

for i in range(0, len(hard_password_list)):
    hard_password += hard_password_list[i]

print(f"Hard version password: {hard_password}")