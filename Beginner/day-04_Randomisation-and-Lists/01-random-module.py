import random
import my_module

# including 1 and 10
random_integer = random.randint(1, 10)
print(f"random_integer: {random_integer}")

# Not including 1
random_number_0_to_1 = random.random()
print(f"random_number_0_to_1: {random_number_0_to_1}")

# Not including 10
random_number_0_to_10 = random.random() * 10
print(f"random_number_0_to_10: {random_number_0_to_10}")

# including 1 and 10
random_float = random.uniform(1, 10)
print(f"random_float: {random_float}")

# imported my_module number
print(f"my_module: {my_module.my_favorite_number}")