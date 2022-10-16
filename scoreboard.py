from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.color("white")
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.create_banner()


    def create_banner(self):
        self.goto(-100, 200)
        self.write(self.score_left, False, align="center", font=('Arial', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.score_right, False, align="center", font=('Arial', 80, 'normal'))

    def update_left(self):
        self.clear()
        self.score_left += 1
        self.create_banner()


    def update_right(self):
        self.clear()
        self.score_right += 1
        self.create_banner()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=('Arial', 60, 'normal'))