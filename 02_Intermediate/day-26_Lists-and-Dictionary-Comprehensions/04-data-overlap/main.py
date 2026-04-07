# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
# You are going to create a list called result which contains the numbers that are common in both files. 

# e.g. if file1.txt contained: 
# 1
# 2
# 3

# and file2.txt contained: 
# 2
# 3
# 4

# result = [2, 3]

# IMPORTANT:  The output should be a list of integers and not strings!

with open("file1.txt", mode="r") as file:
    list_1 = file.readlines()

with open("file2.txt", mode="r") as file:
    list_2 = file.readlines()

result = [int(number) for number in list_1 if number in list_2]

print(result)