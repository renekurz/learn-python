# Python Decorator Function
import time

def delay_decorater(function):
    def wrapper_function():
        time.sleep(2) # It will wait for 2 seconds
        # Do something before
        function()
        # function() # Then it will run twice
        # Do something after

    return wrapper_function

# There are two Options to decorate a function
# Option 1
@delay_decorater
def say_hello():
    print("Hello")

# Option 2
def say_bye():
    print("Bye")

decorated_say_bye = delay_decorater(say_bye)

# Not decorated
def say_greeting():
    print("How are you?")

say_hello()
say_greeting()
decorated_say_bye()

