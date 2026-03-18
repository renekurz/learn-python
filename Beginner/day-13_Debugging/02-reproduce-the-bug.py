from random import randint

# index          0    1    2    3    4    5
dice_numbers = ["1", "2", "3", "4", "5", "6"]

dice_random = randint(1, 6)        # 1. Solution - randint(0, 5)
                                   # or
print(dice_numbers[dice_random-1]) # 2. Solution - [dice_random - 1]

# ERROR - when dice_random = 6
# Because - see dice_numbers index