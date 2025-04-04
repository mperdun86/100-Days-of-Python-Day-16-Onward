from turtle import Turtle

FONT = ('Courier', 80, 'normal')
ALIGNMENT = 'center'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def r_score_increase(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def l_score_increase(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
