from turtle import Turtle

score_cor = (0, 280)
reset = (0, 0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(score_cor)
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(reset)
        self.write("Game is over", False, align="center", font=("Arial", 14, "normal"))
