import art
import os

repeat = True
bid_dictionary = {}
highest_bid = 0
highest_bid_name = ""

while repeat:
    print(art.auction_hammer)
    
    name = input("What's your name?\n")
    bid_price = int(input("How much will you bid?\n"))

    bid_dictionary[name] = bid_price

    other_user_bid = input("Is there anyone who want's to bid? Type 'yes' or 'no': ").lower()

    if other_user_bid == "no":
        for bidder in bid_dictionary:
            if highest_bid < bid_dictionary[bidder]:
                highest_bid = bid_dictionary[bidder]
                highest_bid_name = bidder

        repeat = False
    elif other_user_bid == "yes":
        os.system("clear")
    else:
        print("You typed the wrong string")

print(f"The winner is {highest_bid_name}! He bid ${highest_bid}")