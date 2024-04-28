from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(arg=f"score: {self.score}", align="center", move=False, font=("Courier", 24, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.write(arg=f"score: {self.score}", align="center", move=False, font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over.", align="center", move=False, font=("Courier", 24, "normal"))

    def clear_score(self):
        self.clear()
        self.write(arg=f"score: {self.score}", align="center", move=False, font=("Courier", 24, "normal"))
