# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out.

# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 
# Total = 5 

# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 

# Love Score = 53

true_love = [['t', 'r', 'u', 'e'], ['l', 'o', 'v', 'e']]

def calculate_love_score(name1, name2):
    name1_lower = name1.lower()
    name2_lower = name2.lower()

    # True Count
    word_true = true_love[0] # -> ['t', 'r', 'u', 'e']
    true_count = 0
    for i in range(0, len(name1_lower)):
        true_count += word_true.count(name1_lower[i])

    for i in range(0, len(name2_lower)):
        true_count += word_true.count(name2_lower[i])
    
    print(f"True Count = {true_count}")

    # Love Count
    word_love = true_love[1] # -> ['l', 'o', 'v', 'e']
    love_count = 0
    for i in range(0, len(name1_lower)):
        love_count += word_love.count(name1_lower[i])

    for i in range(0, len(name2_lower)):
        love_count += word_love.count(name2_lower[i])
    
    print(f"Love Count = {love_count}")

    # Output
    total_count = str(true_count) + str(love_count)
    print(f"Love Score = {total_count}")


calculate_love_score("Angela Yu", "Jack Bauer")