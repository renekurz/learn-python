
# TODO-1: IMPORT COLORS FROM IMAGE
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# TODO-2: Copy the output in color_list
color_list = [(249, 248, 244), (243, 250, 246), (250, 244, 248), (240, 245, 250), (234, 225, 84), (195, 8, 69), (231, 54, 132), (197, 77, 17), (113, 177, 213), (194, 164, 14), (216, 162, 102), (29, 104, 167), (34, 187, 113), (14, 24, 64), (20, 29, 169), (231, 224, 7), (215, 134, 177), (201, 32, 132), (14, 182, 210), (231, 167, 197), (127, 188, 161), (10, 48, 28), (54, 20, 10), (40, 132, 75), (140, 218, 203), (108, 92, 210), (235, 64, 34), (131, 217, 231), (183, 17, 8), (11, 96, 53)]

# TODO-3: Draw Painting
import turtle as t
import random

my_turtle = t.Turtle()
t.colormode(255)
t.speed("fastest")

# Field: 10x10
# Dot Size: 20
# Gap: 50

for i in range(10):
    for j in range(10):
        my_turtle.pendown()
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.penup()
        my_turtle.forward(50)
    
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(500)
    my_turtle.right(180)
    

my_screen = t.Screen()
my_screen.exitonclick()