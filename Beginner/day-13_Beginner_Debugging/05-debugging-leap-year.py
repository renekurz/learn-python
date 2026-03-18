# - Read the code in comment
# - Spot the problems 🐞.
# - Modify the code to fix the program.

# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder
# - unless the year is also divisible by 400 with no remainder

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:     # The error was, that there was 4000 instead of 400
                return True
            else:
                return False
        else:
            return False
    else:
        return False