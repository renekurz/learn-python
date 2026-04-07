# - Read the code in comment
# - Spot the problems 🐞.
# - Modify the code to fix the program.

# The code needs to print the solution to the FizzBuzz game.   
# - Your program should print each number from 1 to x where x is the input number. 
# - However when the number is divisible by 3 then instead of printing the number it should print "Fizz".   
# - When the number is divisible by 5, then instead of printing the number it should print "Buzz". 
# - And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".

# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 or number % 5 == 0:
#             print("FizzBuzz")
#         if number % 3 == 0:
#             print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         else:
#             print([number])

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# ERRORS:
# 1. In the first if statement, use 'and' not 'or'
# 2. Change the upcoming if statements to elif
# 3. Remove square brackets at 'number' in the else block