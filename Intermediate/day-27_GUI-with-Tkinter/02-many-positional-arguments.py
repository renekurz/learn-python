def add(*args):
    print(args)
    sum = 0
    for n in args:
        sum += n
    return sum

print(f"1 + 2 + 3 + 4 + 5 = {add(1, 2, 3, 4, 5)}")
print(f"14 + 32 = {add(14, 32)}")
print(f"35 + 93 + 12 = {add(35, 93, 12)}")