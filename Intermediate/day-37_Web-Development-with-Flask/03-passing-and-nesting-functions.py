
# TODO-1: Functions input/functionalitiy/output
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
def calculate(calc_func, a, b):
    return calc_func(a, b)

print(calculate(add, 1, 3))
print("\n")

# TODO-2: Nested Functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    print("I'm past nested_function")

    nested_function()

outer_function()
print("\n")

# TODO-3: Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    print("I'm past nested_function")

    return nested_function

inner_function = outer_function()

inner_function()
