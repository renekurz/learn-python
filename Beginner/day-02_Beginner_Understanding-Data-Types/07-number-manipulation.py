# Round Numbers
print("-----------------------\nRound Numbers\n-----------------------")

bmi = 84 / (1.65 ** 2)
print(bmi)

print(int(bmi))

print(round(bmi))
print(round(bmi, 2))


# Assignment Operators
print("\n-----------------------\nAssignment Operators\n-----------------------")

score = 0
print(score)

score += 1
print(score)

# There are:
# +=    -> add
# -=    -> minus
# *=    -> multiply
# /=    -> divide


# f-Strings
print("\n-----------------------\nf-Strings\n-----------------------")

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}. Your height is = {height}. Are you winning = {is_winning}")