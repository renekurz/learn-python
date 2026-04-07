from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

# Player 1
l_paddle = Paddle(0)
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Player 2
r_paddle = Paddle(1)
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Ball and Scoreboard
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle.paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when r_paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # detect when l_paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()