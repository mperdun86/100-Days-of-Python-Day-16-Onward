from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Consolas", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("chartreuse")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.set_high_score()
        self.get_high_score()
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def set_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.score))


