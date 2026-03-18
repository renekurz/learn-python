enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Scope
player_health = 10

def drink_potion_global():
    potion_strength = 2
    print(potion_strength)
    print(player_health)

drink_potion_global()


# Local Scope
def drink_potion_local():
    potion_strength = 2
    print(potion_strength)

drink_potion_local()