from turtle import Turtle, Screen
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

screen.listen()
screen.onkey(paddle.up_left_paddle, "Up")
screen.onkey(paddle.down_left_paddle, "Down")
screen.onkey(paddle.up_right_paddle, "w")
screen.onkey(paddle.down_right_paddle, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle.paddles[0]) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard.update()
    elif ball.distance(paddle.paddles[1]) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.update()
    if ball.xcor() > 400 or ball.xcor() < -400:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
