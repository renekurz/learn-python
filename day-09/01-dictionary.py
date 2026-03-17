programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# print out a specific value from your key-value pair
print("print out a specific value from your key-value pair")
print(programming_dictionary["Bug"])

# add a new entry
print("\nadd a new entry")
print(programming_dictionary)
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# edit an item in a dictionary
print("\nedit an item in a dictionary")
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# loop through a dictionary
print("\nloop through a dictionary")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
print("\nwipe an existing dictionary")
programming_dictionary = {}
print(programming_dictionary)
