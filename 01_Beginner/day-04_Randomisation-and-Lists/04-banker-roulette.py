import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
random_friend = random.randint(0,4)
print(friends[random_friend])

# Option 2
# print(friends[random.randint(0,4)])

# Option 3
# print(random.choice(friends))