from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def coffee_make_process(coffee):
    coffee_to_make = menu.find_drink(coffee)
    ingredients_sufficient = coffee_maker.is_resource_sufficient(coffee_to_make)

    if not ingredients_sufficient:
        return

    money_sufficient = money_machine.make_payment(coffee_to_make.cost)

    if not money_sufficient:
        return
    
    coffee_maker.make_coffee(coffee_to_make)

while machine_on:
    coffee_input = input(f"What would you like? ({menu.get_items()}): ").lower()

    if coffee_input == "off":
        machine_on = False
    elif coffee_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif coffee_input == "espresso":
        coffee_made = coffee_make_process("espresso")
    elif coffee_input == "latte":
        coffee_made = coffee_make_process("latte")
    elif coffee_input == "cappuccino":
        coffee_made = coffee_make_process("cappuccino")