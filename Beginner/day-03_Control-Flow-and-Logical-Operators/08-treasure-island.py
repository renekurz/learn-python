# Treasure Island Game:
# This is a simple text-based adventure game where the player makes choices
# to find hidden treasure. Based on the user's decisions (left/right, wait/swim,
# and door color), the story progresses and leads either to winning the game
# or a game over scenario.

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

first_choice = input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\": ").lower()
if first_choice == "left":
    second_choice = input("You've come to a lake. There is an island in the middle of the lake?\n\tType \"wait\" to wait for a boat. Type \"swim\" to swim across. Answer: ").lower()
    if second_choice == "wait":
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors.\n\tOne \"red\", one \"yellow\" and one \"blue\". Which colour do you choose: ").lower()
        if third_choice == "red":
            print("You got burned by fire.\nGame Over.")
        elif third_choice == "blue":
            print("You got eaten by beasts.\nGame Over.")
        elif third_choice == "yellow":
            print("Congratulations. You won.")
        else:
            print("Game Over.")
    else:
        print("You got attacked by trout.\nGame Over.")
else:
    print("You fell into a hole.\nGame Over.")