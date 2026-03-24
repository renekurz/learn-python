from turtle import Turtle

STARTING_POSITION = [(-350, 0), (350, 0)]
MOVE_DISTANCE = 20

class Paddle:
    def __init__(self, position):
        new_paddle = Turtle("square")
        new_paddle.color("white")
        new_paddle.shapesize(stretch_wid=5, stretch_len=1)
        new_paddle.penup()
        new_paddle.goto(STARTING_POSITION[position])
        self.paddle = new_paddle

    def up(self):
        new_y = self.paddle.ycor() + MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        new_y = self.paddle.ycor() - MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)