# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# Positional Arguments
greet_with("Alexa", "Texas")
greet_with("Texas", "Alexa")

# Keyword Arguments
greet_with(name="Alexa", location="Texas")
greet_with(location="Texas", name="Alexa")