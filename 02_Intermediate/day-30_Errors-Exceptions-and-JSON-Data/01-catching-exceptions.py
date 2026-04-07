try:
    file = open("a_file.txt")

    a_dictionary = {"key": "value"}
    # print(a_dictionary["not_a_key"]) # Delete the '#' before the print to generate the error
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else: # only runs if there are no errors
    content = file.read()
    print(content)
finally: # runs always
    file.close()
    print("File was closed")