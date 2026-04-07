# "123" is a String, but if you put it into an "int()" function it will be converted to an Integer - we will check it with the type function
print(type(int("123")))

# We learned erlier that "123" + "345" = "123345" but when we put it into an int function it will be calculated
print("123" + "345")
print(int("123") + int("345"))

# These are the different conversion functions:
# int()     -> convert into Integer
# float()   -> convert into Float
# str()     -> convert into String
# bool()    -> convert into Boolean

# EXERCISE
# print("Number of letters in your name: " + len(input("Enter your name "))) -> These will give an error, because len() is from type int but you only can concatenade Strings

# SOLUTION
print("Number of letters in your name: " + str(len(input("Enter your name "))))

# Easier to read:
name = input("Enter your name ")
length_of_name = len(name)
lenght_to_string = str(length_of_name)

print("Number of letters in your name: " + lenght_to_string)