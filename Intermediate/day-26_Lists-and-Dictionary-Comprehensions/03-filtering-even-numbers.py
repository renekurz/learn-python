# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.   

# First, use list comprehension to convert the list_of_strings to a list of integers called numbers.   
# Then use list comprehension again to create a new list called result.
# This new list should only contain the even numbers from the list numbers. 

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(number) for number in list_of_strings]
result = [number for number in numbers if number % 2 == 0]
print(result)