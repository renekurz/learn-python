# Tip Calculator:
# This program calculates how much each person should pay when splitting a bill.
# The user enters the total bill amount, the desired tip percentage, and the
# number of people sharing the bill. The program then adds the tip, divides the
# total by the number of people, and displays the amount each person needs to pay.

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
percentage_tip = float(input("How much tip would you like to give? 10, 12 or 15?\n"))
people_count = float(input("How many people to split the bill?\n"))

each_person_pay = (total_bill + (total_bill * (percentage_tip / 100))) / people_count
each_person_pay_rounded = round(each_person_pay, 2)

print(f"Each person should pay: ${each_person_pay_rounded}")