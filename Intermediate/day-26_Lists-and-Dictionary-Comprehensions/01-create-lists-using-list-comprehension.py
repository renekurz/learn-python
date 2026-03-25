numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(f"numbers: {numbers}")
print(f"new_numbers: {new_numbers}\n")

name = "Alexa"
letters_list = [letter for letter in name]
print(f"name: {name}")
print(f"letters_list: {letters_list}\n")

range_list = [num * 2 for num in range(1, 5)]
print(f"range_list: {range_list}\n")

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]
print(f"names: {names}")
print(f"short_names: {short_names}")
print(f"long_names: {long_names}\n")