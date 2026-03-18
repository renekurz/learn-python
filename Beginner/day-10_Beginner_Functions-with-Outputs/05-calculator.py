import art
import os

repeat_calculation = True
continue_calculation = True

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while repeat_calculation:
    print(art.calculator_logo)

    first_number = float(input("What's the first number? "))

    while continue_calculation:
        for operator in operations:
            print(operator)

        pick_operator = input("Pick an operation: ")
        second_number = float(input("What's the next number? "))
        total = float(operations[pick_operator](first_number, second_number))

        if not total:
            os.system("clear")
            print("You entered a wrong operator")
            break

        print(f"{first_number} {pick_operator} {second_number} = {total}")

        continue_calculation = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")

        if continue_calculation == "n":
            continue_calculation = False
            os.system("clear")
        elif continue_calculation == "y":
            first_number = total