print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
    
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.\n")
    
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")