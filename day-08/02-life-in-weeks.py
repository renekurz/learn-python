# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format: You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
# Example Input: 56
# Example Output: You have 1768 weeks left.

weeks_in_year = 52
life_expectancy = 90

def life_in_weeks(age):
    actual_years = life_expectancy - age
    weeks_left = actual_years * weeks_in_year

    print(f"You have {weeks_left} weeks left.")

life_in_weeks(20)