from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    
    for _ in range(num_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for shape_side_n in range(3, 11):
    my_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)

my_screen = Screen()
my_screen.exitonclick()