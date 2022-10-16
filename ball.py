from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("normal")
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor()

        new_x += self.x_move
        new_y += self.y_move
        self.goto(new_x, new_y)

    def move_after_miss_left(self):
        self.goto(0,0)
        self.x_move *= -1
        self.y_move *= -1

    def move_after_miss_right(self):
        self.goto(0,0)
        self.x_move *= -1
        self.y_move *= -1
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1