def calculate(n, **kwargs):
    print(f"n = {n}\nkwargs = {kwargs}")
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"n = {n}\n")


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        # You need kwargs.get("...") so you don't get an Error, if the keyword doesn't exist
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

nissan_gtr = Car(make="Nissan", model="GT-R", seats=2)
print(f"make: {nissan_gtr.make}\nmodel: {nissan_gtr.model}\nseats: {nissan_gtr.seats}\n")

vw = Car(make="VW", color="Red")
print(f"make: {vw.make}\ncolor: {vw.color}")