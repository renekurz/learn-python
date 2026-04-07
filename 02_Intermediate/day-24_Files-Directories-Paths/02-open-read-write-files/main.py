# You have to close the file manually
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()  

# when you open the file with "with" it will close automatically
with open("my_file.txt") as file:
	contents = file.read()
	print(contents)

# write to the file - everything will be deleted in the file
with open("my_writing_file.txt", mode="w") as file:
	file.write("New text.")

# write to the file without deleting everything - "a" is like .append at a list
with open("my_writing_file.txt", mode="a") as file:
	file.write("\nMy name is Tom.")

# create a new file - if the name of the file doesn't exist, it will be created
with open("new_file.txt", mode="w") as file:
	file.write("This is a new file.")