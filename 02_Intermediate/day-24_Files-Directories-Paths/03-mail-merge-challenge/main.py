
# TODO: Create a letter using starting_letter.txt for each name in invited_names.txt
#       Replace the [name] placeholder with the actual name.
#       Save the letters in the folder "ReadyToSend"

with open("Input/Names/invited_names.txt", mode="r") as names:
    invited_names = names.readlines()

    for name_idx in range(0, len(invited_names)):
        invited_names[name_idx] = invited_names[name_idx].strip("\n")

with open("Input/Letters/starting_letter.txt", mode="r") as letter:
    dummy_letter = letter.read()

for name in invited_names:
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as mail:
        mail.write(dummy_letter.replace("[name]", name))