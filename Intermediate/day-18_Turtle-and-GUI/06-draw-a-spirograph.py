import turtle as t
import random

my_turtle = t.Turtle()
my_turtle.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)

draw_spirograph(5)

my_screen = t.Screen()
my_screen.exitonclick()