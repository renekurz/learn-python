# Between 1 and 10; not including 10
print("Between 1 and 10; not including 10")
for number in range(1, 10):
    print(number)

# Between 1 and 11; not including 11; 3 Steps each time
print("\n\nBetween 1 and 11; not including 11; 3 Steps each time")
for number in range(1, 11, 3):
    print(number)

# add all numbers between 1 and 100; including 100
print("\n\nAdd all numbers between 1 and 100; including 100")
calculated_number = 0
for number in range(1, 101):
    calculated_number += number

print(f"calculated_number: {calculated_number}")