# Bad way
print("---------- BAD WAY ----------")
enemies = 1

print(f"(before func) enemies outside function: {enemies}")

def increase_enemies_bad():
    global enemies # need to modify global scope
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies_bad()
print(f"(after func) enemies outside function: {enemies}")


# Good way
print("\n---------- GOOD WAY ----------")
enemies = 1

print(f"(before func) enemies outside function: {enemies}")

def increase_enemies_good(enemy):
    print(f"enemies inside function: {enemy + 1}")
    return enemy + 1

enemies = increase_enemies_good(enemies)
print(f"(after func) enemies outside function: {enemies}")