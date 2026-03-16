states_of_america = ["Delaware", "Pennsylvania"]

# first to last
print("first: " + states_of_america[0])
print("second: " + states_of_america[1])

# last to first
print("first (negative): " + states_of_america[-1])
print("second (negative): " + states_of_america[-2])

# Change an Item
states_of_america[1] = "Pencilvania"
print(states_of_america)

# Add an Item
states_of_america.append("New Jersey")
print(states_of_america)

# Adds more Items to the end of the list
states_of_america.extend(["Georgia", "Texas"])
print(states_of_america)