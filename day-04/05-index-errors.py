states_of_america = ["Delaware", "Pennsylvania"]

print(len(states_of_america))

# IndexError: list index out of range
# Because len is 2 and the last Element in the list is at index 1. This is because the first one is at index 0.
# print(states_of_america[len(states_of_america)])

# You have to subtract len with 1
print(states_of_america[len(states_of_america) - 1])
