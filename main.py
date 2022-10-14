from turtle import Turtle, Screen
from paddle import Paddle

turtle = Turtle()
screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)


paddle = Paddle()

screen.listen()
screen.onkey(paddle.up_left_paddle, "Up")
screen.onkey(paddle.down_left_paddle, "Down")
screen.onkey(paddle.up_right_paddle, "w")
screen.onkey(paddle.down_right_paddle, "s")

game_is_on = True
while game_is_on:
    screen.update()
    # for one_paddle in paddle.paddles:
    #     if one_paddle.ycor() == 600:
    #



screen.exitonclick()
