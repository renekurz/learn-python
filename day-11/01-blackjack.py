import os
import art
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
repeat_game = True

def add(game_cards):
    total = 0
    for card in game_cards:
        total += card
    return total

def print_finish(player, dealer):
    print(f"Your Cards: {player}, total score: {add(player)}")
    print(f"Dealer Cards: {dealer}, total score: {add(dealer)}\n")

def extend_cards(cards_to_extend, number_to_extend):
    for i in range(int(number_to_extend)):
        cards_to_extend.append(random.choice(cards))

def blackjack():
    continue_game = True

    while continue_game:
        os.system("clear")

        dealer_cards = []
        player_cards = []

        print(art.card_logo)

        # TODO-1: Dealer gets 2 Cards and Player gets 2 Cards
        extend_cards(dealer_cards, 2)
        extend_cards(player_cards, 2)

        # TODO-2: Calculate the current total from Dealer and Player
        current_total_dealer = add(dealer_cards)
        current_total_player = add(player_cards)

        # TODO-3: Show Player Cards and only one Card from the Dealer
        print(f"Your Cards: {player_cards}, current score: {current_total_player}")
        print(f"Dealer Cards: [{dealer_cards[0]}, X]\n")

        # TODO-4: Blackjack
        #   1. If the Dealer has Blackjack and the Player not - Dealer wins
        #   2. If the Player has Blackjack and the Dealer not - Player wins
        #   3. If both have Blackjack                         - It's a draw
        if current_total_dealer == 21 and current_total_player == 21:
            print("It's a draw!")
            print_finish(player_cards, dealer_cards)
            continue_game = False
            break
        elif current_total_dealer == 21:
            print("BLACKJACK!\nDealer wins! You lose!")
            print_finish(player_cards, dealer_cards)
            continue_game = False
            break
        elif current_total_player == 21:
            print("BLACKJACK!\nYou win! Dealer lose!")
            print_finish(player_cards, dealer_cards)
            continue_game = False
            break

        # TODO-4: Hit or Stand
        # TODO-5: Over 21
        # TODO-6: Player over 21 but has 11 so it become 1
        continue_hit_or_stand = True

        while continue_hit_or_stand:
            hit_or_stand = input("Type 'h' for a Card, or type 's' for stand: ")

            if hit_or_stand == "h":
                extend_cards(player_cards, 1)
                current_total_player = add(player_cards)
                print(f"Your Cards: {player_cards}, current score: {current_total_player}\n")

                if current_total_player > 21:
                    if 11 in player_cards:
                        player_cards.remove(11)
                        player_cards.append(1)

                        current_total_player = add(player_cards)

                        print(f"Since you have an 11 so it become 1, otherwise you'll go over 21")
                        print(f"Your Cards: {player_cards}, current score: {current_total_player}\n")
                    else:
                        print(f"Dealer wins! You have over 21.")
                        print_finish(player_cards, dealer_cards)
                        break

            elif hit_or_stand == 's':
                continue_hit_or_stand = False
            else:
                print("You typed the wrong key")
                break
        
        if current_total_player > 21:
            continue_game = False
            break

        # TODO-7: Player Stand - Dealer has to get Cards till over or equal to 17
        while True:
            extend_cards(dealer_cards, 1)
            current_total_dealer = add(dealer_cards)
            print(f"Dealer Cards: {dealer_cards}, current score: {current_total_dealer}")

            if current_total_dealer >= 17:
                break

        # TODO-8: Analyze
        total_dealer = add(dealer_cards)
        total_player = add(player_cards)

        if total_dealer > 21:
            print(f"You win! Dealer has over 21.")
            print_finish(player_cards, dealer_cards)
        elif total_dealer == total_player:
            print(f"It's a draw.")
            print_finish(player_cards, dealer_cards)
        elif total_dealer > total_player:
            print(f"Dealer wins! You lose!")
            print_finish(player_cards, dealer_cards)
        elif total_player > total_dealer:
            print(f"You win! Dealer lose!")
            print_finish(player_cards, dealer_cards)

        continue_game = False


while repeat_game:
    blackjack()

    # TODO-9: Ask if the player wants to play again
    repeat_game_input = input("Do you want to play again? 'y' for yes, 'n' for no: ")

    if repeat_game_input == 'n':
        repeat_game = False