from turtle import Turtle, Screen

UP = 90
DOWN = 0


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.paddle_position = [(350, 0), (-350, 0)]
        self.create_paddle()

    def create_paddle(self):
        for position in self.paddle_position:
            new_paddle = Turtle("square")
            new_paddle.color("white")
            new_paddle.shapesize(5, 1)
            new_paddle.penup()
            new_paddle.goto(position)
            self.paddles.append(new_paddle)
            print("Paddle created")

    def up_left_paddle(self):
        if self.paddles[0].ycor() >= 250:
            pass
        else:
            self.paddles[0].sety(self.paddles[0].ycor() + 20)


    def down_left_paddle(self):
        if self.paddles[0].ycor() <= -240:
            pass
        else:
            self.paddles[0].sety(self.paddles[0].ycor() - 20)


    def up_right_paddle(self):
        if self.paddles[1].ycor() >= 250:
            pass
        else:
            self.paddles[1].sety(self.paddles[1].ycor() + 20)


    def down_right_paddle(self):
        if self.paddles[1].ycor() <= -240:
            pass
        else:
            self.paddles[1].sety(self.paddles[1].ycor() - 20)



