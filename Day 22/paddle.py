from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(starting_position)

        self.shapesize(stretch_wid=5,stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


