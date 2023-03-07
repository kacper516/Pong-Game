from turtle import Screen, Turtle

import paddle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

"""SCREEN"""
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # I stop animation to move turtle to right corner

# it'll be useful while someone earn a point

l_paddle_cords = (-350, 0)
r_paddle_cords = (350, 0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

# Right paddle move
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

# Left paddle move
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with up or down wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()  # to change the direction of ball in function move

    """detect collision with paddles, the value of 50 is, 
    because ball has got a width of 20 pixels and paddle too and 50 works fine nad smooth"""
    if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and abs(ball.xcor()) > 320:
        ball.bounce_x()

    """detect when paddle misses, 380 works fine, because paddles has got height of 350px 
    and can go up and down about 20 px, so when the ball x.cor is bigger than 380 paddles must miss the ball"""

    # right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
        paddle.reset_paddles(l_paddle, r_paddle)

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
        paddle.reset_paddles(l_paddle, r_paddle)

screen.exitonclick()
