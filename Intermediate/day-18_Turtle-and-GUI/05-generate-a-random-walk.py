import turtle as t
import random

my_turtle = t.Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(15)
my_turtle.speed("fastest")

t.colormode(255)
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    color = (r, g, b)
    return color

for _ in range(200):
    my_turtle.color(random_color())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(directions))

my_screen = t.Screen()
my_screen.exitonclick()