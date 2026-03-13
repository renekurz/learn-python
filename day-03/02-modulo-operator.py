# Even number 12 % 2 == 0 -> no remaining
print(12 % 2)

# Check odd or even
number = int(input("What is the number you want to check?\n"))
odd_or_even = number % 2

if odd_or_even == 0:
    print("Your number is even")
else:
    print("Your number is odd")