# Read the code in comment - Spot the problems 🐞. 

# Modify the code to fix the program. 
# Fix the code so that it works and passes the tests when you submit.

# def odd_or_even(number):
#     if number % 2 = 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."

def odd_or_even(number):
    if number % 2 == 0:     # The error was, that there was only one '=' instead of '=='
        return "This is an even number."
    else:
        return "This is an odd number"