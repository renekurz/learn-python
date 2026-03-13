print("Welcome to the rollercoaster!")

height = int(input("What is your height?\n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    
    if age < 12:
        print("Your ticket will cost $5")
    elif age <= 18:
        print("Your ticket will cost $7")
    else:
        print("Your ticket will cost $12")
else:
    print("You are too small to ride the rollercoaster")