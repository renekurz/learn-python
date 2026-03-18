
# TODO-1: Hot Coffees
#   Espresso, Latte, Cappuccino
#   Ingredients:
#       Espresso: 50ml Water, 18g Coffee
#       Latte: 200ml Water, 24g Coffee, 150ml Milk
#       Cappuccino: 250ml Water, 24g Coffee, 100ml Milk
#   Prices:
#       Espresso: $1.50
#       Latte: $2.50
#       Cappuccino: $3.00

hot_coffees = {
    "Espresso": {
        "Water": 50,
        "Coffee": 18,
        "Price": 1.5,
    },
    "Latte": {
        "Water": 200,
        "Coffee": 24,
        "Milk": 150,
        "Price": 2.5,
    },
    "Cappuccino": {
        "Water": 250,
        "Coffee": 24,
        "Milk": 100,
        "Price": 3,
    },
}

# TODO-2: Coffee Machine
#   Start Resources:
#       Water: 300ml
#       Milk: 200ml
#       Coffee: 100g
#   Coin Operated:
#       Penny: $0.01
#       Nickel: $0.05
#       Dime: $0.10
#       Quarter: $0.25

coffee_machine = {
    "Water": {
        "left": 300,
        "unit": "ml",
    },
    "Milk": {
        "left": 200,
        "unit": "ml",
    },
    "Coffee": {
        "left": 100,
        "unit": "g",
    },
    "Money": {
        "left": 0.0,
        "unit": "$",
    },
}

coins = {
    "Penny": 0.01,
    "Nickel": 0.05,
    "Dime": 0.1,
    "Quarter": 0.25,
}

# TODO-3: Program Requirements
#   1. Print report
#       What Resources has left (Water, Milk, Coffee, Money)
#       type 'report' to get this information
#   2. Check resources sufficient
#       e.g. Sorry, there is not enough water
#   3. Process coins
#       Insert coins (e.g. How many quarters?)
#       Give Change
#       If not enough money to cover drink, give the money back (e.g. Sorry that's not enough money. Money refunded)
#   4. Make Coffee
#       update resources and coins in machine

def make_coffee(water, coffee, milk):
    coffee_machine["Water"]["left"] -= water
    coffee_machine["Coffee"]["left"] -= coffee
    coffee_machine["Milk"]["left"] -= milk

def collect_coins(coffee):
    cost = hot_coffees[coffee]["Price"]

    input_quarter = float(input("How many quarters ($0.25)? ")).__round__(2)
    input_dime = float(input("How many dimes ($0.10)? ")).__round__(2)
    input_nickel = float(input("How many nickels ($0.05)? ")).__round__(2)
    input_penny = float(input("How many pennies ($0.01)? ")).__round__(2)

    money_given = (input_quarter * coins["Quarter"]) + (input_dime * coins["Dime"]) + (input_nickel * coins["Nickel"]) + (input_penny * coins["Penny"])
    change = cost - money_given

    if change > 0:
        print(f"Sorry, that's not enough money. {coffee} costs ${cost}. You gave ${money_given}. Here is your refund.")
        return False

    if change < 0:
        print(f"Here is ${(change * -1).__round__(2)} dollars in change.")

    coffee_machine["Money"]["left"] += cost
    return True

def look_for_ingredients(coffee):
    coffee_ingredients = hot_coffees[coffee]
    water = coffee_ingredients["Water"]
    ground_coffee = coffee_ingredients["Coffee"]

    if coffee == "Latte" or coffee == "Cappuccino":
        milk = coffee_ingredients["Milk"]

        if coffee_machine["Milk"]["left"] < milk:
            print("Sorry, there is not enough milk.")
            return False

    if coffee_machine["Water"]["left"] < water:
        print("Sorry, there is not enough water.")
        return False
    
    if coffee_machine["Coffee"]["left"] < ground_coffee:
        print("Sorry, there is not enough coffee.")
        return False
    
    enough_coins = collect_coins(coffee)

    if not enough_coins:
        return False
    
    make_coffee(water, ground_coffee, milk)
    return True

machine_on = True

while machine_on:
    coffee_made = False
    coffee_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_input == "off":
        machine_on = False
    elif coffee_input == "report":
        for resource in coffee_machine:
            if resource == "Money":
                print(f"{resource}: {coffee_machine[resource]["unit"]}{coffee_machine[resource]["left"]}")
            else:
                print(f"{resource}: {coffee_machine[resource]["left"]}{coffee_machine[resource]["unit"]}")
    elif coffee_input == "espresso":
        coffee_made = look_for_ingredients("Espresso")
    elif coffee_input == "latte":
        coffee_made = look_for_ingredients("Latte")
    elif coffee_input == "cappuccino":
        coffee_made = look_for_ingredients("Cappuccino")

    if coffee_made:
        print(f"Here is your {coffee_input.title()}. Enjoy!")