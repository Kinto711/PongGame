from turtle import Turtle, Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



turtle = Turtle()
screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

turtle.color("white")
turtle.shape("square")
turtle.shapesize(stretch_wid=800, stretch_len=0.1, outline=None)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

# score_left_position = (-270, 270)
# score_right_position = (270, 270)
#
# left_banner = scoreboard.create_banner(score_left_position)
# right_banner = scoreboard.create_banner(score_right_position)

screen.listen()
screen.onkey(paddle.up_left_paddle, "Up")
screen.onkey(paddle.down_left_paddle, "Down")
screen.onkey(paddle.up_right_paddle, "w")
screen.onkey(paddle.down_right_paddle, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(paddle.paddles[0]) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    elif ball.distance(paddle.paddles[1]) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # detect when right paddle missing
    if ball.xcor() > 400:
        scoreboard.update_left()

        ball.move_after_miss_left()

    # detect when left paddle missing
    if ball.xcor() < -400:
        scoreboard.update_right()

        ball.move_after_miss_right()



screen.exitonclick()
